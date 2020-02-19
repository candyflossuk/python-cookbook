"""
Script showing how to search for and replace a text
pattern in a string
"""
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'

text.replace('yeah', 'yep')  # 'yep, but no, but yep, but no, but yep'

# For more complicated patterns use sub() methods in the re module
# Write 11/27/2012 as 2012-11-27
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13'
"""
First argument to sub() is the pattern to match
Second argument is replacement pattern
Backslashed digits refer to capture group numbers
"""

# For repeated subs of the same pattern, consider compiling it first
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13'


def change_date(m):
    """
    For more complicated substitutions specify a substitution callback function
    :param m:
    :return:
    """
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


datepat.sub(change_date, text)
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013'

"""
As input, argument to substituion callback is a match object 
(as returned by match() or find()

Use the .group() method to extract specific parts of the match.

If you want to find out how many substituions were made in addition
to getting the replacement text use re.subn() 
"""
newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext  # 'Today is 2012-11-27. PyCon starts 2013-3-13'
n  # 2
