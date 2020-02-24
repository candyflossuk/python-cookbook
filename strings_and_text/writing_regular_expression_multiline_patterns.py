"""
Script showing how to match a block of text using a regular expression,
spanning multiple lines

This problem occurs in patterns that use (.) to match any character but
do not account for newlines.
"""
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
                multiline comment */'''

comment.findall(text1)  # [' this is a comment ']
comment.findall(text2)  # []

# to fix, add support for new lines
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
# [' this is a \n                multiline comment ']

"""
In the pattern (?:.|\n) - the patterns specifies the non capture group
where it defines a group for the purpose of matching but not captured
separately or numbered

The re.compile() function accepts a flag, re.DOTALL which is also useful. 
It makes the . in regex match all characters including new lines i.e
"""
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)
# [' this is a \n                multiline comment ']

"""
Using DOTALL flag works for simple cases - problematic for 
extremely complex patterns or mix of separate regex that 
are combined to tokenize. 

Given a choice its best to define your regex so it works without flags
"""
