#!/usr/bin/python3

import os, sys
from PIL import Image

img_dir = r"/home/geeobcr/convert_images/images"
output_dir = r"/opt/icons/"
size = (128,128)
rotation = 90

# Create Directory if doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process all files in img_dir
for f in os.listdir(img_dir):
    if not f.startswith("."):
        outfile = os.path.join(output_dir, f)

        try:
            img = Image.open(os.path.join(img_dir,f))
            img = img.rotate(rotation).resize(size)
            img.convert('RGB').save(outfile, "JPEG")
        except OSError:
            print("unable to convert file", f)