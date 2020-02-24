"""
This script shows the use of regular expressions when
unicode characters are present.

By default re (module) is already programmed with knowledge
of unicode character classes
"""
import re

# ASCII digits
num = re.compile('\d+')
num.match('123')  # <re.Match object; span=(0, 3), match='123'>

# Arabic digits
num.match('\u0661\u0662\u0663')  # <re.Match object; span=(0, 3), match='١٢٣'>

"""
To include specific Unicode characters in patterns
use standard escape sequences for unicode characters
\uFFFFF or \UFFFFFFF

Below regex matches all characters in some Arabic code pages
 """
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

"""
When matching and searching its good to normalize and sanitize
all text to a standard form - take special cases into account 
like case-insensitive matching
"""
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)
# <re.Match object; span=(0, 6), match='straße'>
pat.match(s.upper())  # no match
s.upper()  # 'STRASSE'

""" 
Mixing Unicode and regex is a good way to mess your head up!
If your doing it seriously - consider using third-party regex library
which has full unicode case folding support and other 
nice features to make regular expressions more powerful.
"""
