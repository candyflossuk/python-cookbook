"""
This script shows how to decode and encode data using base64 encoding
"""
import base64

# Encode
s = b'hello'
a = base64.b64encode(s)

# Decode
base64.b64encode(a)

"""
Base64 encoding is only meant to be used on byte-orientated data such as byte strings and byte arrays.
The output of encoding is always a byte string. If you are mixing base-64 encoded data with unicode text 
you may have to perform extra decoding
"""
a = base64.b64encode(s).decode('ascii')

# When decoding base64 - both byte strings and unicode strings can be supplied. However, unicode strings can only
# contain ascii

