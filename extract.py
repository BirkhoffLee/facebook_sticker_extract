#!/usr/bin/env python

import os
from PIL import Image

table = [4, 4, 4, 3]
stickerPath = "./stickers.png"
outputDirFull = "./output/full/"
outputDirSticker = "./output/sticker/"
outputDirCustom = "./output/custom/"

# Custom-sized
wantedImageSize = (180, 180)    # The actual image size (px)
wantedStickerSize = (100, 100)  # The sticker's size in the actual image (px)

###

sticker_width = 288 # (px)
sticker_height = 288 # (px)
sticker_offset = 24 # (px)

###

if not os.path.exists(outputDirFull):
    os.makedirs(outputDirFull)
if not os.path.exists(outputDirSticker):
    os.makedirs(outputDirSticker)
if not os.path.exists(outputDirCustom):
    os.makedirs(outputDirCustom)


img = Image.open(stickerPath)
count = 0

for colIndex, row in enumerate(table):
    for rowIndex in range(row):
        count += 1
        cropped = img.crop((sticker_offset   + sticker_width  *  rowIndex, # left
                            sticker_offset   + sticker_height *  colIndex, # up
                            - sticker_offset + sticker_width  * (rowIndex + 1), # right
                            - sticker_offset + sticker_height * (colIndex + 1))) # down

        # Full-sized version
        cropped.save(outputDirFull + str(count) + ".png")

        # Sticker-sized version
        cropped.thumbnail((120, 120))
        cropped.save(outputDirSticker + str(count) + ".png")

        # Custom-sized version
        offset_width = (wantedImageSize[0] - wantedStickerSize[0]) / 2
        offset_height = (wantedImageSize[1] - wantedStickerSize[1]) / 2
        cropped.thumbnail(wantedStickerSize)
        new = Image.new("RGBA", wantedImageSize, (0, 0, 0, 0))
        new.paste(cropped, (offset_width, offset_height))
        new.save(outputDirCustom + str(count) + ".png")
