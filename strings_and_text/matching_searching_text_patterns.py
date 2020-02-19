"""
Script to demonstrate how to match or search text
for a specific pattern

If text is literal - you can use str.find(), str.endswit() etc
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
text == 'yeah'  # False

# Match at start or end
text.startswith('yeah')
# True

text.endswith('no')
# False

# Search for the location of the first occurence
text.find('no')  # 10

"""
For more complicated matching use regular expressions and the re
module. To match 11/27/2012 for example this is how you would do it...
"""

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# no

# If you are to perform a lot of matches using the same pattern,
# it pays to precompile the regular expression into a pattern object

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# yes

if datepat.match(text2):
    print('yes')
else:
    print('no')

# no

"""
match() always tries to find the match at the start of a string.
If you want to search all occurrences use findall()
"""

text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
datepat.findall(text)  # ['11/27/2012', '3/13/2013']

# Common to introduce capture groups by enclosing parts of pattern in parens
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# Capture groups simplify subsequent processing
# as contents of each group can be extracted individually

m = datepat.match('11/27/2012')
m  # <re.Match object; span=(0, 10), match='11/27/2012'>

m.group(0)  # 11/27/2012
m.group(1)  # 11
m.group(2)  # 27
m.group(3)  # 2012
m.groups()
month, day, year = m.groups()

# Final all matches
datepat.findall(text)  # [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# 2012-11-27
# 2013-3-13

"""
findall() searches the text and finds all the matches
returning them as a list. To get them iteratively use
finditer()
"""
for m in datepat.finditer(text):
    print(m.groups())

# ('11', '27', '2012')
# ('3', '13', '2013')

"""
First compile a pattern using re.compile()
Then use methods such as match() findall() or finditer()

When specifying patterns its common to use raw strings.
Backslash is left uninterpreted - which can be useful in 
context of regular expressions.

match() method only checks beginning of a string.
This may result in matches you are not expecting
"""
m = datepat.match('11/27/2012abcdef')
m  # <re.Match object; span=(0, 10), match='11/27/2012'>
m.group()  # '11/27/2012'

# For exactch matches make sure pattern includes $ end marker
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')  # <re.Match object; span=(0, 10), match='11/27/2012'>

# If doing simple text matching/searching you can skip compilation
re.findall(r'(\d+)/(\d+)/(\d+)', text)
[('11', '27', '2012'), ('3', '13', '2013')]

"""
If you are going to do lots of matching or searching - it 
often pays to compile the pattern. The module level functions
keep a cache of recently compiled patterns - not a huge 
performance hit - but you'll save a few lookups and extra processing.
"""

