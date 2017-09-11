import argparse
import pathlib

from .io import read
from .structs import png_header


def save_images(filename):
    path = pathlib.Path(filename)
    buffer = path.open('rb')
    icon_directory = read(buffer)
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar='FILE')
    args = parser.parse_args()

    save_images(args.filename)
