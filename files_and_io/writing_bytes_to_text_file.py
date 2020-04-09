"""
This script shows how to write raw bytes to a file opened in text mode

This is simple to do - simply write the byte data to the files underlying buffer as shown below
"""
import sys

sys.stdout.write(b'Hello\n') # Causes a TypeError
sys.stdout.buffer.write(b'Hello\n')

"""
Binary data can be read from a text file by reading from its buffer attribute instead.

THe I/O system is built from layers. Text files are constructed by adding a unicode
encoding/decoding layer on top of a buffer binary-mode file. The buffer attribute
simply points at this underlying file. If you access it - you bypass the encoding/decoding layer
"""
