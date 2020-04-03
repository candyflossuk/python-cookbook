"""
This script shows how to feed a text or binary string to code that
has been written to operate on file like objects

This is done by using the io.StringIO() and io.BytesIO() classes
to create file like objects that operate on string data
"""
import io

s = io.StringIO()
s.write('Hello World\n')

print('This is a test', file=s)

# Get all of the data written so far
s.getvalue()  # 'Hello World\nThis is a test\n'

# Wrap a file interface around the existing string
s = io.StringIO('Hello\nWorld\n')
s.read(4)
s.read()

# The io.StringIO class should only be used for text. If you are using binary data use io.BytesIO
s = io.BytesIO()
s.write(b'binary data')
s.getvalue()  # b'binary data'

"""
These two classes are most useful in scenarios where you need to mimic a normal file - such as unit tests

They don't have a proper integer-file-descriptor and wont work with code that use files such
as 'file' 'pipe' or 'socket' at the system-level
"""
