#!/usr/bin/env python

from PIL import Image
import os

img = Image.open("trash_doves.png")
img.thumbnail((576, 576))

offset = 3
cols = [4,4,4,3]
outputDir = "./output"
count = 0

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for index in range(len(cols)):
    for _ in range(cols[index]):
        count += 1
        cropped = img.crop((12 + 144 * _, 12 + 144 * index, 144 * (_ + 1) - 12, 144 * (index + 1) - 12)) # 120x120
        cropped.save(outputDir + "/" + str(count) + ".png")