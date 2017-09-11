from .models import FileHeader, IconMeta, CursorMeta
from .structs import header_struct, image_meta_struct


def read(buffer):
    h = FileHeader(*header_struct.unpack(buffer.read(header_struct.size)))

    if h.image_type == 1:
        _class = IconMeta
    else:
        _class = CursorMeta

    return [
        _class(*image_meta_struct.unpack(buffer.read(image_meta_struct.size)))
        for i in range(h.num_images)
    ]
