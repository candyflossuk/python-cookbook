"""
Script to match a text pattern using reg ex, but identifying the shortest possible
match.

This pattern is useful when matching text inside a pair of starting
and ending delimiters i.e a quoted string
"""
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no"'
str_pat.findall(text1)  # ['no']

text2 = 'Computer says "no." Phone says "yes"'
str_pat.findall(text2)
# ['no." Phone says "yes']

"""
In this - pattern(r'\"(.*)\"') is attempting to match 
text enclosed in quotes. * is greedy so matching is based 
on finding longest possible match.

To fix this add the ? modifier after the * operator
in the pattern
"""
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

# This makes it nongreedy and produces the shortest match

"""
This pattern addresses one of the more common problems when 
writing regex involving the . character. In a reg ex pattern
the dot will match any character except new line - however if you
bracket the dot with start and end text (quote for example)
matching will try to find the longest possible match to the 
pattern. This causes multiple occurrences of the starting 
or end text to be skipped and included in the results of 
longer match. Adding ? right after * or + forces matching
algorithm to look for the shortest possible match.

"""

