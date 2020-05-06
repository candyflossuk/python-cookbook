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
    [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]


# To write this to a binary file of a defined structure use the following
def write_polys(filename, polys):
    # determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)

    with open(filename, "wb") as f:
        f.write(struct.pack("<iddddi", 0x1234, min_x, min_y, max_x, max_y, len(polys)))

    for poly in polys:
        size = len(poly) * struct.calcsize("<dd")
        f.write(struct.pack("<i", size + 4))
        for pt in poly:
            f.write(struct.pack("<dd", *pt))


# Call it with polygon data
write_polys("polys.bin", polys)

# To read the result - use struct.unpack() reversing the opeartion above
def read_polys(filename):
    with open(filename, "rb") as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = struct.unpack(
            "<iddddi", header
        )
        polys = []
        for n in range(num_polys):
            (pbytes,) = struct.unpack("<i", f.read(4))
            poly = []
            for m in range(pbytes):
                pt = struct.unpack("<dd", f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys


# The code above is pretty messy - the code in coming days focuses on
# defining the structure of the file - and everything happening under the covers

"""
Struct can unpack data to a tuple that contains headers and other data structures -another way 
to represent information is through the use of a class - the example below shows how to 
do this.
"""


class StructField:
    # Descriptor representing a simple structure field
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


"""
The code shown uses a descriptor to represent each structure field.

Each descriptor contains a struct compatible format code along with a byte offset into an underlying memory buffer.

In get() method - struct.unpack_from() is used to unpack a value from the buffer without having to make extra slices
or copies.

The Structure class just serves as a base class that accepts some byte data and stores it as the underlying
memory buffer used by the StructField descriptor. The use of memoryview() in this class serves a purpose 
that will become clear later in this example.

Using this code you can now define a structure as a high level class that mirrors the information found
in the tables that described the expected file format.
"""


class PolyHeader(Structure):
    file_code = StructField("<i", 0)
    min_x = StructField("<d", 4)
    max_x = StructField("<d", 12)
    min_y = StructField("<d", 20)
    max_y = StructField("<d", 28)
    num_polys = StructField("<i", 36)


# Here is an example of how to use this to read the header from the polygon data
f = open("polys.bin", "rb")
phead = PolyHeader(f.read(40))
phead.file_code == 0x1234
phead.min_x
phead.max_x
phead.min_y
phead.max_y
phnead.num_polys

"""
This approach has some annoyances - the code is verbose and requires the user to specify a lot of low level details.
The resulting class is also missing common convenience methods such as a method to compute total size of the 
structure.

When a class is overly verbose you might consider the use of a class decorator or metaclass. 
One feature of a metaclass is that it can be used to fill in a low of low level implementation details,
taking the burden off the user. 

Below a metaclass and reformulation of the Structure class is shown.
"""


class StructureMeta(type):
    # Metaclass that automatically creates StructField descriptors

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, "_fields_", [])
        byte_order = ""
        offset = 0
        for format, fieldname in fields:
            if format.startswith(("<", ">", "!", "@")):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
            setattr(self, "struct_size", offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self.buffer = bytedata

    # classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


# Using this is now a lot easier
class PolyHeader(Structure):
    _fields_ = [
        ("<i", "file_code"),
        ("d", "min_x"),
        ("d", "min_y"),
        ("d", "max_x"),
        ("d", "max_y"),
        ("i", "num_polys"),
    ]


# From file makes it easier to read the data from a file without knowing details about the size or structure of the data
f = open("polys.bin", "rb")
phead = PolyHeader.from_file(f)
phead.file_code = 0x1234
phead.mix_x
phead.min_y
phead.max_x
phead.max_y
phead.num_polys


"""
Once a metaclass is introduced - you can build more intelligence into it. 
If you want to add support for nested binary structures for example - this 
is how you would reformulate the metaclass along with a new supporting descriptor that allows it
"""


class NestedStruct:
    """
    Descriptor representing a nested structure.

    Used to overlay another structure definition over a region of memory.
    This is done by taking a slice of the original memory buffer and using it to 
    instantiate the given structure type.

    Since the underlying memory buffer was initialized as a memoryview this slicing
    does not incur any extra memory copies. Instead it is just an overlay on the
    original memory.

    To avoid repeated instantiations the descriptor then stores the resulting
    inner structure object on the instance.
    """

    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[
                self.offset : self.offset + self.struct_type.struct_size
            ]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    """
    Metaclass that automatically creates StructField descriptors
    """

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, "_fields_", [])
        byte_order = ""
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(("<", ">", "!", "@")):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)

        setattr(self, "struct_size", offset)


"""
Using this we can write code as follows...
"""


class Point(Structure):
    _fields_ = [("<d", "x"), ("d", "y")]


class PolyHeader(Structure):
    _fields_ = [("<i", "file_code"), (Point, "min"), (Point, "max"), ("i", "num_polys")]


# This works as you expect
f = open("polys.bin", "rb")
phead = PolyHeader.from_file(f)
phead.file_code = 0x1234

# So far we have dealt with fixed size sections - to deal with variable size sections we can write
# a new class that represents a chunk of binary data along with a utility function for interpreting the
# contents in different ways


class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        """
        Reads a size-prefixed chunk of data from a file,
        common in many file formats.
        Accepts a structure format code containing the encoding of the size
        The includes_size argument specifies whether the number of bytes includes
        the size of header or not.
        :param f: 
        :param size_fmt: 
        :param includes_size: 
        :return: 
        """
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        (sz,) = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off : off + size]
                yield code(data)


# Usage shown below
f = open("polys.bin", "rb")
phead = PolyHeader.from_file(f)
phead.num_polys
polydata = [SizedRecord.from_file(f, "<i") for n in range(phead.num_polys)]
polydata

# To interpret the contents of theSizedRecord instances use iter_as() method
for n, poly in enumerate(polydata):
    print("Polygon", n)
    for p in poly.iter_as("<dd"):
        print(p)

for n, poly in enumerate(polydata):
    print("Polygon", n)
    for p in poly.iter_as(Point):
        print(p.x, p.y)

# putting the above together - here is a read_polys() function


class Point(Structure):
    _fields_ = [("<d", "x"), ("d", "y")]


class PolyHeader(Structure):
    _fields_ = [("<i", "file_code"), (Point, "min"), (Point, "max"), ("i", "num_polys")]


def read_polys(filename):
    polys = []
    with open(filename, "rb") as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, "<i")
            poly = [(p.x, p.y) for p in rec.iter_as(Point)]
            polys.append(poly)
    return polys


"""
This implementation is strong based on the idea of lazy-unpacking. When an instance of Structure is 
created, the __init__() merely creates a memoryview of the supplied byte data and does nothing else.

No unpacking or other structure related operations take place at this time. One motivation
for taking this approach is that you may only be interested in small parts of the binary structure.
This allows you to only access the parts of the structure that you need to

To achieve this the StructField descriptor class is used. Each attribute the user lists
in _fields_ gets converted to a StructField descriptor that stores the associated structure format code and
byte offset into the stored buffer. 

The StructureMeta metaclass is what creates these descriptors automatically when various structure classes are 
defined. The main reason for using a metaclass is to make it easy for a user to specify a structure format
with a high level description without worrying about low level details.

A subtle aspect of the StructureMeta metaclass is that it makes byte order sticky. That is, if any attribute 
specifies a byte order (< for little endian or > big endian) that ordering applies to all fields that follow. This 
avoids extra typing but also makes it possible to switch in the middle of a definition.

The use of a memoryview() avoids memory copies. When structures start to nest, memoryviews can be used to overlay 
different parts of the structure definition on the same region of memory. This is subtle but concerns the slicing
behaviour of a memoryview verus byte array. 

Slicing byte array - gets a copy of data - with memory view slices overlay the existing memory - thus
it is more efficient.


"""
