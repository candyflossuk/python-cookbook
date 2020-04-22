"""
This script shows how to parse an XML document using XML namespaces
"""
from xml.etree.ElementTree import iterparse

# Once a document is parsed - some queries dont work so easily because everything is verbose
# Some queries that work
doc.findtext('author')
doc.find('content')

# A query involving a namespace (does not work)
doc.find('content/html')

# Works if fully qualified
doc.find('content/{http://www.w3.org/1999/xhtml}html')
# Everything must be fully qualified, you can simplify by wrapping namespace handling in a utility class


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'

    def __call__(self, path):
        return path.format_map(self.namespaces)

# usage
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
doc.find(ns('content/{html}html'))
doc.findtext(ns('content/{html}html/{html}head/{html}title'))

"""
Parsing XML documents that contain namespaces can be messy, the XMLNamespaces
class is menat to clean it up by using shortened namespace names

There is no mechanism in the basic ElementTree parser. You can 
get more information about the scope of namespace processing if you are willing to use
iterparse() 
"""
for evt, elem in iterparse('ns2.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)

"""
If text you are parsing makes use of namespaces in addition to other advanced XML
features your best using lxml library instead of ElementTree - it provides
better support for validating documents against a DTD, better XPath support.
"""
