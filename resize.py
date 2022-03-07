#!/usr/bin/env python3

import os
import sys
from collections import namedtuple

from gooey import Gooey, GooeyParser
from PIL import Image

"""
    Instagram can host a single image, or a grouping of images that we create a "gallery" image in the size for Instagram - 1080 x 1080 px
    Facebook image size - 1200 x630 px
    Facebook event - for the sale listing on the calendar - 1920 x 1005 pixels
    Event Brite Image - 2160 x 1080px
    Twitter image - so many sizes to choose from on this platform - I can use the 1080 x 1080 square.
"""
Site = namedtuple("Site", "name hint max_x max_y")
sites = [
    Site("Instagram", "ig", 1080, 1080),
    Site("Facebood", "fb", 1200, 630),
    Site("FB_event", "fbe", 1920, 630),
    Site("EventBrite", "eb", 2160, 1080),
    Site("Twitter", "tw", 1080, 1080)
]

def resize_image(image, specs):
    cur_x, cur_y = image.size
    if cur_x < specs.max_x and cur_y < specs.max_y:
        return image, specs.hint
    # we want to keep the aspect ratio
    x_ratio = float(specs.max_x) / float(cur_x)
    y_ratio = float(specs.max_y) / float(cur_y)
    ratio = min(x_ratio, y_ratio)
    new_x = int(cur_x * ratio)
    new_y = int(cur_y * ratio)
    resized_image = image.resize((new_x, new_y))
    # get rid of alpha channel, since we store as jpeg
    # based on https://stackoverflow.com/a/48248432
    if resized_image.mode in ("RGBA", "P"):
        resized_image = resized_image.convert("RGB")
    return resized_image, specs.hint


def generate_files(fname):
    base, _ = os.path.splitext(fname)
    for site in sites:
        im = Image.open(fname)
        new_im, hint = resize_image(im, site)
        new_fname = f"{base}-{hint}.jpg"
        new_im.save(new_fname)

@Gooey(show_restart_button=False,
       return_to_config=True,
       clear_before_run=True)
def parse_args(argv=None):
    parser = GooeyParser(description="Resize images for Social Media")
    parser.add_argument('Filename', widget="FileChooser")
    args = parser.parse_args()
    return args

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    args = parse_args(argv)
    if args.Filename:
        generate_files(args.Filename)


if __name__ == "__main__":
    main(sys.argv[1:])
