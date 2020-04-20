"""
This script shows how to take data in a Python dictionary and turn it into XML

xml.etree.ElementTree can be used to create XML documents
"""
from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape, unescape


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
e

# The result of the conversion is an Element instance. For I/O it is easy to convert this to byte string
tostring(e)  # b'<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'

# If you want to attach attributes to an element, use set() method
e.set('_id', '1234')
tostring(e)  # b'<stock _id="1234"><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'

# DO NOT JUST CREATE STRINGS - THIS IS A RECIPE FOR ANNOYANCE LATER!

# As a note - to escape and unescape characters in XML use escape() and unescape() as follows()
escape('<spam>')  # '&lt;spam&gt;'
unescape(_) # '<spam>'

"""
Another good reason to use Element(s) is that they can be combiend to make larger documents. 
You don't have to worry about it parsing an XML test. 
"""
