"""
This script shows how to read complicated binary encoded data that
contains nested and/or variable sized records. Such data includes
images,videos etc

The struct module can be used to decode and encode almost any kind
of binary data structure. To illustrate the kind of data in question see below.
"""
import struct
import itertools

polys = [
          [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
          [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
          [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
        ]


# To write this to a binary file of a defined structure use the following
def write_polys(filename, polys):
    # determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)

    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))

    for poly in polys:
        size = len(poly) * struct.calcsize('<dd')
        f.write(struct.pack('<i', size+4))
        for pt in poly:
            f.write(struct.pack('<dd', *pt))

            
# Call it with polygon data
write_polys('polys.bin', polys)

# To read the result - use struct.unpack() reversing the opeartion above
def read_polys(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = struct.unpack('<iddddi', header)
        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys

# The code above is pretty messy - the code in coming days focuses on
# defining the structure of the file - and everything happening under the covers
