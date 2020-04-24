"""
This script shows how to decode a string of
hex digits into a byte string or encode the inverse

You can do this using the binascii module
"""
import binascii
import base64

s = b'hello'

# Encode as hex
h = binascii.b2a_hex(s)

# Decode back to bytes
binascii.a2b_hex(h)

# Similar functionallity exists in the base64 module
h = base64.b16encode(s)
base64.b16encode(s)

# Main difference between the two is case folding
# base64.b16encode and decode functions only operate with uppercase hex
# binascii works with either case, output is always a byte string
