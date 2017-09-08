#!/usr/bin/env python3
import pathlib
import struct
import sys

from attr import attrs, attrib


header_struct = struct.Struct('<2x2H')
image_meta_struct = struct.Struct('<3Bx2H2I')
png_header = struct.Struct('>B3s4B')


@attrs(frozen=True, slots=True)
class FileHeader:

    image_type = attrib()
    num_images = attrib()


@attrs(slots=True, frozen=True)
class IconMeta:

    width = attrib()
    height = attrib()
    num_colours = attrib()
    colour_planes = attrib()
    bits_per_pixel = attrib()
    size = attrib()
    offset = attrib()


@attrs(slots=True, frozen=True)
class CursorMeta:

    width = attrib()
    height = attrib()
    num_colours = attrib()
    hotspot_x = attrib()
    hotspot_y = attrib()
    size = attrib()
    offset = attrib()


def main(filename):
    path = pathlib.Path(filename)
    buffer = path.open('rb')
    h = FileHeader(*header_struct.unpack(buffer.read(header_struct.size)))

    if h.image_type == 1:
        _class = IconMeta
    else:
        _class = CursorMeta

    icon_directory = [
        _class(*image_meta_struct.unpack(buffer.read(image_meta_struct.size)))
        for i in range(h.num_images)
    ]
    for i, meta in enumerate(icon_directory):
        buffer.seek(meta.offset)
        image = buffer.read(meta.size)
        p = png_header.unpack_from(image)
        if p == (137, b'PNG', 13, 10, 26, 10):
            extension = 'png'
        else:
            extension = 'bmp'
        print(f'{extension}: {meta.width}x{meta.height}')
        with path.with_suffix(f'.{i}.{extension}').open('wb') as fh:
             fh.write(image)


if __name__ == '__main__':
    main(sys.argv[1])
