"""
This script show how to read an XML document make changes then write it back as xml

xml.etree.ElementTree module makes it easy to perform such tasks.
"""
from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')
root = doc.getroot()

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>..</nm>
root.getchildren().index(root.find('nm'))
# 1
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)

"""
Modifying the structure of an XML document is straightforward
you must remember that all modifications are generally made 
to the parent element, treating it as if it were a list.

For example - if you remove an element, it is removed from 
its immediate parent using the parent's remove() method. 
If you insert or append new elements, you also use insert()
and append() on the parent.

Elements can also be manipulated using indexing and slicing operations
such as element[i] or element[i:j]
"""
