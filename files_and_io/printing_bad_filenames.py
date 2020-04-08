"""
This script shows how to print filenames that cause
a UnicodeEncodeError exception which gives the error message
'surrogates' not allowed

When printing filenames of unknown origin use this convention
"""
import os
import sys

filename = ('somefile.txt')


def bad_filename(filename):
    return repr(filename)[1:-1]


try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))

"""
This problem is rare - but pretty annoying. When python encounters a situation where 
there are bad filenames where it cannot turn the file name into a proper string it
takes an undecodable byte value \xhh in a filename and maps it into a so called
surrogate encoding represented by Unicode character \udchh. For example:
The filename 'bäd.txt' encoded as latin instead of utf-8 would come out as follows:
"""
files = os.listdir('.')
files
# ['b\udce4d.txt']

# When you want to output the filename you will get issues i.e
for name in files:
    print(name)

# will throw UnicodeEncodeError: surrogates not allowed - this is because \udce4 is part of a surrogate pair.
# to fix take corrective action when a bad filename is encountered

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(filename))

# Another option is to re-encode the value in some way like so:


def bad_filename_reencoded(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')
