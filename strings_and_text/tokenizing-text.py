"""
This script shows you how to parse a string from left to right into a stream
of tokens.
"""
import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
# to tokenize you need to identify the kind of pattern to match. i.e sequence of pairs

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# to do this - first step is to define all possible tokens incl whitespace by regex using named capture groups
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

"""
In these patterns the ?P<TOKENNAME> convention is used to assign a name to the pattern (to be used later)

Next we can use scanner() method of pattern objects to to tokenize. This creates
a scanner object - repeated calls to match() are then made. These calls step through
the supplied text one match at a time.
"""

scanner = master_pat.scanner('foo = 42')
scanner.match()  # <re.Match object; span=(3, 4), match=' '>
_.lastgroup, _.group()  # ('WS', ' ')
scanner.match()  # <re.Match object; span=(4, 5), match='='>
_.lastgroup, _.group()
scanner.match()  # <re.Match object; span=(5, 6), match=' '>
# .. etc etc

# The below shows how to put this into 'proper' packaged code

Token = namedtuple('Token', ['type','value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example usage
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# To filter the token stream you can define a generator function or expression - to filter whitespace tokens...
tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)

# The order of tokens is important, when matching re tries to match in order specified
# If pattern happens to be a stubstring of longer pattern - make sure longer pattern is first
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat.re.compile('|'.join([LE, LT, EQ]))

# Watch out for patterns that form substrings
PRINT = r'(P<PRINT>print)'
NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

# More more advanced tokenizing use PyParsing or PLY
