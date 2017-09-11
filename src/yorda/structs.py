import struct


header_struct = struct.Struct('<2x2H')
image_meta_struct = struct.Struct('<3Bx2H2I')
png_header = struct.Struct('>B3s4B')
