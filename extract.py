#!/usr/bin/env python

from PIL import Image
import os

img = Image.open("trash_doves.png")

offset = 3
cols = [4,4,4,3]
outputDir = "./output"
count = 0

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for index in range(len(cols)):
    for _ in range(cols[index]):
        count += 1
        cropped = img.crop((_ * 160, index * 160 + offset, (_  + 1) * 160, (index + 1) * 160 + offset))
        (width, height) = cropped.size
        new = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        new.paste(cropped)
        new.save(outputDir + "/" + str(count) + ".png")