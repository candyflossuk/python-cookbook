"""
Script showing how to search and possibly replace text in
a case insensitive manner.

To perform case-insensitive text operations - use re module.
Use re.IGNORECASE flag
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
# ['PYTHON', 'python', 'Python']

# replacing text won't match the case - a support function is required


def matchcase(word):
    def replace(m):
        text_matched = m.group()
        if text_matched.isupper():
            return word.upper()
        elif text_matched.islower():
            return word.lower()
        elif text_matched[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# usage of above function
re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)

"""
Simple cases - use re.IGNORECASE to perform case-insensitive matching.
May not work out the same for Unicode matching
"""
