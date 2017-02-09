#!/usr/bin/env python

cols = [4, 4, 4, 3]
outputDirFull = "./output/full/"
outputDirSticker = "./output/sticker/"
outputDirCustom = "./output/custom/"

###

from PIL import Image
import os

if not os.path.exists(outputDirFull):
    os.makedirs(outputDirFull)
if not os.path.exists(outputDirSticker):
    os.makedirs(outputDirSticker)
if not os.path.exists(outputDirCustom):
    os.makedirs(outputDirCustom)


img = Image.open("trash_doves.png")
count = 0

for colIndex in range(len(cols)):
    for rowIndex in range(cols[colIndex]):
        count += 1
        cropped = img.crop((24 + 288 * rowIndex, 24 + 288 * colIndex, 288 * (rowIndex + 1) - 24, 288 * (colIndex + 1) - 24)) # 240x240

        # Full-sized version
        cropped.save(outputDirFull + str(count) + ".png")
        ####

        # Sticker-sized version
        cropped.thumbnail((120, 120))
        cropped.save(outputDirSticker + str(count) + ".png")
        ####

        # Customized-sized version
        wantedDaveSize = (100, 100)
        wantedImageSize = (180, 180)
        cropped.thumbnail(wantedDaveSize)
        new = Image.new("RGBA", wantedImageSize, (0, 0, 0, 0))
        new.paste(cropped, ((wantedImageSize[0] - wantedDaveSize[0]) / 2, (wantedImageSize[1] - wantedDaveSize[1]) / 2))
        new.save(outputDirCustom + str(count) + ".png")
        ####