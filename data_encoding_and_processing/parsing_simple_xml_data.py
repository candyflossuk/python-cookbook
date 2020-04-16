"""
This script shows how to extract data from an XML document

To do this use xml.etree.ElementTree
"""
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pudDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

"""
xml.etree.ElementTree.parse() parses the entire XML document into a document object.
From there you can use find, iterfind, findtext to search. The arguments are the names of a 
specific tag.

When specifying the tags you need to take overall document structure into account.
The tagname supplied is relative to the start of the document 

Each element represented by the ElementTree module has a few essential 
attributes and methods that are useful when parsing. The tag 
attribute contains the name of hte tag, the text attribute contains the text get() 
can be used to extract the attributes

For more advanced applications you can use lxml - it uses the same interface as ElementTree.
It is extremely fast and supports validation, XSLT and XPath.
"""
