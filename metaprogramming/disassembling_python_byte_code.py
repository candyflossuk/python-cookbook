"""
This script shows how to find out what your python code is doing under the hood
showing the low level byte code used by the interpreter

To do this the 'dis' module can be used
"""
import dis
import opcode


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
    print("Blastoff!")


dis.dis(countdown)
"""
  5     >>    0 LOAD_FAST                0 (n)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               4 (>)
              6 POP_JUMP_IF_FALSE       28
  6           8 LOAD_GLOBAL              0 (print)
             10 LOAD_CONST               2 ('T-minus')
             12 LOAD_FAST                0 (n)
             14 CALL_FUNCTION            2
             16 POP_TOP
  7          18 LOAD_FAST                0 (n)
             20 LOAD_CONST               3 (1)
             22 INPLACE_SUBTRACT
             24 STORE_FAST               0 (n)
             26 JUMP_ABSOLUTE            0
  8     >>   28 LOAD_GLOBAL              0 (print)
             30 LOAD_CONST               4 ('Blastoff!')
             32 CALL_FUNCTION            1
             34 POP_TOP
             36 LOAD_CONST               0 (None)
             38 RETURN_VALUE
"""

# Raw byte code can be interpreted by the dis() function
countdown.__code__.co_code
b"|\x00d\x01k\x04r\x1ct\x00d\x02|\x00\x83\x02\x01\x00|\x00d\x038\x00}\x00q\x00t\x00d\x04\x83\x01\x01\x00d\x00S\x00"

# To interpret code yourself, you need to use some of the constants defined in the opcode module
c = countdown.__code__.co_code
opcode.opname[c[0]]
opcode.opname[c[0]]

# A generator can be created that takes raw byte code and turns it into opcodes and arguments
def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)


# Usage
for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)

"""
It is possible to replace the raw byte code of any function. This often results in interpreter crashes - however
for advanced optimization this may be suitable. 
"""
