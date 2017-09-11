from attr import attrs, attrib


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
