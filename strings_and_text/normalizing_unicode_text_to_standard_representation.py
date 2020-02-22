"""
Script showing that when working with unicode you need to make
sure that all strings have the same underlying representation
"""
import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

s1 == s2

len(s1)
len(s2)

"""
The same text is presented in two forms. The first 
uses the fully composes n (in unicode) The second uses the latin
n followed by an a "~" combining character (U+0303)

Having multiple representations is not great where you are comparing
strings. To fix - you should normalize the representation using
the unicodedata module
"""

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

t1 == t2  # True

print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
t3 == t4

print(ascii(t3))
# 'Spicy Jalapen\u0303o'

"""
First arg to normalize() specifies how you 
want string to be normalized.

NFC - fully composed - use single code point if possible
NFD - characters should be fully composed with use of combining
characters

Python also supports NFKC NFKD - adding extra compatibility features 
"""

s = '\ufb01' # single char
s  # 'ﬁ'

unicodedata.normalize('NFD', s)
# 'ﬁ'

# Combined letters are broken apart (in below...)
unicodedata.normalize('NFKD', s)
# 'fi'

unicodedata.normalize('NFKC', s)
# 'fi'

"""
Normalization is important in code to ensure consistency.
Especially when received as part of user input - where
you have no control of encoding.

It also works as a method of sanitizing and filtering text -
for example removing diacritical marks from text
"""

t1 = unicodedata.normalize('NFD', s1)

''.join(c for c in t1 if not unicodedata.combining(c))  # 'Spicy Jalapeno'
# combining() function tests character to see if its combining character
# there are other modules for matching categories, digits etc
