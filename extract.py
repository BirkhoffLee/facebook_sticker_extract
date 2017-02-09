#!/usr/bin/env python

import os
from PIL import Image

cols = [4, 4, 4, 3]
outputDirFull = "./output/full/"
outputDirSticker = "./output/sticker/"
outputDirCustom = "./output/custom/"

###

sticker_width = 288
sticker_height = 288
sticker_offset = 24

###

if not os.path.exists(outputDirFull):
    os.makedirs(outputDirFull)
if not os.path.exists(outputDirSticker):
    os.makedirs(outputDirSticker)
if not os.path.exists(outputDirCustom):
    os.makedirs(outputDirCustom)


img = Image.open("trash_doves.png")
count = 0

for colIndex in enumerate(cols):
    for rowIndex in range(cols[colIndex]):
        count += 1
        cropped = img.crop((sticker_offset + sticker_width * rowIndex,
                            sticker_offset + sticker_height * colIndex,
                            sticker_width * (rowIndex + 1) - sticker_offset,
                            sticker_height * (colIndex + 1) - sticker_offset))

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

        offset_width = (wantedImageSize[0] - wantedDaveSize[0]) / 2
        offset_height = (wantedImageSize[1] - wantedDaveSize[1]) / 2
        cropped.thumbnail(wantedDaveSize)
        new = Image.new("RGBA", wantedImageSize, (0, 0, 0, 0))
        new.paste(cropped, (offset_width, offset_height))
        new.save(outputDirCustom + str(count) + ".png")
        ####
