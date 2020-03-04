"""
Parse text based on a set of grammar rules and perform
actions - or build abstract syntax tree representing input.

Grammar is small - write parser as opposed to using a framework

Below is a simple recipe that shows how to build a recursive descent expression evaluator
"""
import re
import collections

# Token specification
NUM     = r'(?P<NUM>\d+)'
PLUS    = r'(?P<PLUS>\+)'
MINUS   = r'(?P<MINUS>-)'
TIMES   = r'(?P<TIMES>\*)'
DIVIDE  = r'(?P<DIVIDE>/)'
LPAREN  = r'(?P<LPAREN>\()'
RPAREN  = r'(?P<RPAREN>\))'
WS      = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


# Parser
class ExpressionEvaluator:
    """
    Implementation of a recursive descent parser. Each method
    implements a single grammar rule. Use the ._accept() method
    to test and accept the current lookahead token. Use the
    ._expect()
    method to exactly match and discard the next token on the input
    (or raise a SyntaxError if it doesn't match).
    """

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Next symbol tokenized
        self._advance()         # Load first lookahead token
        return self.expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammar rules follow
    def expr(self):
        "expression ::= term { ('+'|'-') term }*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


# example usage of ExpressionEvaluator class
e = ExpressionEvaluator()
e.parse('2')  # 2
e.parse('2 + 3')  # 5
e.parse('2 + (3 + 4) * 5')  # 37
# e. parse('2 + (3 + * 4)')  # SyntaxError

# To construct a simple parse tree you could do something like this...

class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term { ('+'|'-') term }"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        'factor ::= NUM | ( expr )'

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

"""
A recursive simple descent parser takes every grammar rule and turns it into 
a function or method

for example...

expr ::= term { ('+'|'-') term} *

    term ::= factor { ('*'|'/') factor |*
    
    factor ::= '(' expr ')'
        | NUM
        
can be turned into something like this
"""
class ExpressionEvaluator:

    def expr(self):
        return None  # Do nothing

    def term(self):
        return None  # Do nothing

    def factor(self):
        return None  # Do nothing

"""
The task of each method is fairly straight forward. Walk from left to right
over each part of the grammar rule, consuming tokens. 

The goal of each method is to consume the rule or generate a syntax error. To
do this the following implementation techniques are used

* If the next symbol in the rule is the name of another grammar rule - you call the method 
with the same name. This is the 'descent' part of the algo - control descends into
another grammar rule. Sometimes these rules will involve calls to methods that are 
already executing (e.g - the call to expr in the factor ::= '(' expr ')' rule).
This is the reccursive part of the algorithm also.

* If the next symbol in the rule has to be a specific symbol (e.g '(' ) you look at the
next token to check for an exact match. Where there is no match its a syntax error. 
The _expect() method is used for htis

* If the next symbol in the rule could be a choice (i.e + or - ) you have to check
the next token for each possibility and advanced only if a match is made. This is 
where we use _accept() method, the _accept method() is like the _expect() method 
but weaker. If no match is made it backs off without raising an error - allowing
for further checks to be made

* For grammar rules where there are repeated parts such as:
    expr ::= term { ('+'|'-') term }*) the repetition gets implemented in a while loop.
The loop will collect or process all of the repeated items until no more are found.

* Once an entire grammar rule has been consumed, each method returns some kind of result back 
to the caller. Eventually all results are combined together in the topmost grammar rule method that executes.

* One limitation of recursive descent parsers is that they can't be written for grammar rules involving
any kind of left recursion.
e.g     items ::= items ',' item
            | item
"""
# To implement left recursion you could use: - APART FROM IT RESULTS IN INFINITE REUCRSION

def items(self):
    itemsval = self.items()
    if itemsval and self.accept(','):
        itemsval.append(self.item())
    else:
        itemsval = [ self.item() ]

"""
For complicated grammars use PyParsing or PLY.
"""

from ply.lex import lex
from ply.yacc import yacc

# Token list
tokens = ['NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']

# Ignored characters
t_ignore = ' \t\n'

# Token spec (regex)
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'


# Token processing functions
def t_NUM(t):
    # r'\d+'
    t.value = int(t.value)
    return t


# Error handler
def t_error(t):
    print('Bad character: {!r}'.format(t.value[0]))
    t.skip(1)


# Build the lexer
lexer = lex()


# Grammar rules and handler functions
def p_expr(p):
    """
    expr : expr PLUS term
        | expr MINUS term
    :param p:
    :return:
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_term(p):
    """
    expr : term
    :param p:
    :return:
    """
    p[0] = p[1]


def p_term(p):
    """
    term : term TIMES factor
        | term DIVIDE factor
    :param p:
    :return:
    """
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    """
    term : factor
    :param p:
    :return:
    """
    p[0] = p[1]


def p_factor(p):
    """
    factor : NUM
    :param p:
    :return:
    """
    p[0] = p[1]


def p_factor_group(p):
    """
    factor: LPAREN expr RPAREN
    :param p:
    :return:
    """
    p[0] = p[2]


def p_error(p):
    print('Syntax error')

parser = yacc()

# mechanics of running the parser are abstracted.

parser.parse('2')
parser.parse('2 + 3')
parser.parse('2+(3+4)*5')

















