"""
This script shows how to extract data from a huge xml document
using as little memory as possible.

When thinking of large data sets - think iterators and generators.
The following function can be used to incrementally process huge
XML files using a small memory footprint.

Use data from:
https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD
"""
from xml.etree.ElementTree import iterparse, parse
from collections import Counter


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem) # Helps save memory - causes previously yielded element to be removed from parent
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

# To test use a big data set
potholes_by_zip = Counter()

doc = parse('potholes.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

"""
Problem with this is that it reads and parses the entire XML file into 
memory. Using the code above uses a memory footprint of 450MB the below uses just 7MB
"""
pot_holes_by_zip = Counter()

data = parse_and_remove('potholes.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

"""
Primary downside to this recipe is runtime performance. This version of code reads entire document into 
memory runs twice as fast as the one that does it incrementally. However it requires 60x less memory. 
Pick your poison!
"""
