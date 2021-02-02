"""
This script imports a python module via url.

This solution installs an instance of a finder object UrlMetaFinder
as the last entry in the sys.meta_path. When
modules are imported the finders in sys.meta_path are stepped thru
in order to locate the module. UrlMetaFinder becomes a finder of last
resort when the normal options are exhausted.

UrlMetaFinder wraps around a user-specified URL. Internally
said finder builds a set of valid links by scraping them from the URL. When
the import is done - the module name is compared against this set of
known links. If a match is found, a separate UrlModuleLoader class is
used to load source code from the remote machine and create the resulting
module object.
"""
import sys
import importlib.abc
import imp
import types
from types import ModuleType
from typing import Optional
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

# Debugging
import logging

log = logging.getLogger(__name__)


# Get links from a given URL
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                attrs = dict(attrs)
                links.add(attrs.get("href").rstrip("/"))

    links = set()
    try:
        log.debug("Getting links from %s" % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode("utf-8"))
    except Exception as e:
        log.debug("Could not get links %s" % e)
    log.debug("links: %r", links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl: UrlModuleLoader(baseurl)}

    def find_module(self, fullname: str, path=None):
        log.debug("find_module: fullname=%r, path=%r", fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split(".")
        basename = parts[-1]
        log.debug("find_module: baseurl=%r, basename=%r", baseurl, basename)

        # Check link cache
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        # Check if it's a package
        if basename in self._links[baseurl]:
            log.debug("find_module: trying package %r", fullname)
            fullurl = self._baseurl + "/" + basename
            # Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_mdule(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug("find_module: package %r loaded", fullname)
            except ImportError as e:
                log.debug("find_module: package failed. %s", e)
                loader = None
            return loader

        # Normal module
        filename = basename + ".py"
        if filename in self._links[baseurl]:
            log.debug("find_module: module %r found", fullname)
            return self._loaders[baseurl]
        else:
            log.debug("find_module: module %r not found", fullname)
            return None

    def invalidate_caches(self) -> None:
        log.debug("invalidating link cache")
        self._links.clear()


# Module loader for a URL
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module: ModuleType) -> str:
        return "<urlmodule %r from %r>" % (module.__name__, module.__file__)

    # Required method
    def load_module(self, fullname: str) -> types.ModuleType:
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition(".")[0]
        exec(code, mod.__dict__)
        return mod

    # Optional extensions
    def get_code(self, fullname: str) -> Optional[types.CodeType]:
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), "exec")

    def get_data(self, path):
        pass

    def get_filename(self, fullname: str):
        return self._baseurl + "/" + fullname.split("."[-1] + ".py")

    def get_source(self, fullname: str) -> Optional[str]:
        filename = self.get_filename(fullname)
        log.debug("loader: reading %r", filename)
        if filename in self._source_cache:
            log.debug("loader: cached %r", filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode("utf-8")
            log.debug("loader: %r loaded", filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug("loader: %r ailed %s", filename, e)
            raise ImportError("Can't load %s" % filename)

    def is_package(self, fullname: str) -> bool:
        return False


# Package Loader for a URL
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname: str):
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname: str):
        return self._baseurl + "/" + "__init__.py"

    def is_package(self, fullname: str) -> bool:
        return True


# Utility functions for installing/uninstalling the loader
_installed_meta_cache = {}


def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug("%r installed on sys.meta_path", finder)


def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug("%r removed from sys.meta.path", finder)


"""
Usage:

import fib # will fail

import urlimport
urlimport.install_meta('http://localhost:15000')
import fib
import spam
import grok.blah
grok.blah.__file__


So what is this doing?
We are installing an instance of a special finder object called UrlMetaFinder
in the last entry in sys.meta_path. When modules are imported the finders in sys.meta_path
are consulted in order to locate the module.

Another approach is to write a hook that plugs directly into sys.path variable recognizing
certain directory patterns
"""


class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug("find_loader: %r", fullname)
        parts = fullname.split(".")
        basename = parts[-1]
        # Check link cache
        if self._links is None:
            self._links = []
            self._links = _get_links(self._baseurl)

        # Check if it's a package
        if basename in self._links:
            log.debug("find_loader: trying package %r", fullname)
            fullurl = self._baseurl + "/" + basename
            # Attempt to load the package
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug("find_loader: package %r loaded", fullname)
            except ImportError as e:
                log.debug("find_loader: %r is a namespace package", fullname)
                loader = None
            return (loader, [fullurl])

        # A normal module
        filename = basename + ".py"
        if filename in self._links:
            log.debug("find_loader: module %r found", fullname)
            return (self._loader, [])
        else:
            log.debug("find_loader: module %r not found", fullname)
            return (None, [])

    def invalidate_caches(self) -> None:
        log.debug("invalidating link cache")
        self._links = None
