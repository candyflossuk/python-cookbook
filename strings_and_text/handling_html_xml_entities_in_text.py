"""
Script shows how to replace HTML and XL entities with
their corresponding text - also shows how to produce text
but escape certain characters

To do this you can use html.escape() function
"""
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print(s)
# Elements are written as "<tag>text</tag>".
print(html.escape(s))
# Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

# Disable escaping of quotes
print(html.escape(s, quote=False))
# Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

# To emit text as ASCII and embed character code entities for non-ASCII
# characters - you can use errors = xmlcharrefreplace

s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')
# b'Spicy Jalape&#241;o'

"""
To replace entities in text a different approach is required. If you are 
processing HTML or XML try using a parser first. Normally these 
take care of replacing values for you during parsing.

If you want to replace the entities manually - you can use utility functions
associated with the parsers
"""
s = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
p.unescape(s)
# 'Spicy Jalapeño'

t = 'The prompt is &gt;&gt;&gt;'
unescape(t)
# 'The prompt is >>>'

# Always consider a proper parser such as html.parser or xml.etree.ElementTree

