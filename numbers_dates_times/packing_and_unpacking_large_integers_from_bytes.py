"""
This script focuses on unpacking a byte string to its integer value.
Or converting a large integer to a byte string
"""
import struct

# 16 element byte string that holds a 128 bit integer
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# To interpret bytes as an integer use int.from_bytes() and specify byte ordering
len(data)
int.from_bytes(data, 'little')  # 69120565665751139577663547927094891008
int.from_bytes(data, 'big')  # 94522842520747284487117727783387188

# To convert large int back to bytes use int.to_bytes() specifying number and order of bytes
x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')  # b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x.to_bytes(16, 'little')  # b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# Doing the above is not a common operation, however it sometimes arises in certain application domains
# i.e Crypto or networking

"""
As an laternative - you can unpack values using the struct module. 
The size of integers that can be unpacked by struct is limited. 
You need to unpack multiple values and combine them to create the final 
value
"""
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo  # 94522842520747284487117727783387188

"""
The specification of the byte order - 'little' or 'big' indicates whether 
the bytes that make up the integer value are listed from the least to most 
significant or the other way round. This is easy to view using a carefully
crafted hex value
"""
x = 0x01020304
x.to_bytes(4, 'big')  # b'\x01\x02\x03\x04'
x.to_bytes(4, 'little')  # b'\x04\x03\x02\x01'

"""
If you try to pack an integer into a byte string but it won't fit
you will get an error. You can use int.bit_length() to determine
how many bits you need to store a value if needed.
"""
x = 523 ** 23
x.to_bytes(16, 'little')  # OverflowError
x.bit_length() # 208
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes +=1
x.to_bytes(nbytes, 'little')  # b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\xa2\xc8\xd9R\xb5\xd0'

