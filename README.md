# facebook_sticker_extract
This tool extracts every frame of an animated Facebook sticker.

# Usage
1. Open a Messenager chat session and send your friend the animated sticker you'd like to extract.
2. If you want a high DPI sticker zoom in to 200%.
3. Right-click the sticker you just sent. Click "inspect" and you can see:

  ![Background Image URL](README-assets/background-url.png)

4. Right-click on that highlighted URL, click "open".
5. Right-click on the new-opened image, save it under your clone of this repository and name it `sticker.png`
6. Open that image and take a look. For example:

  ![An example stickerset](README-assets/example-stickers.png)

  The format of this sticker is:

  ```
  X  X  X
  X  X  X
  X  X  X
  ```
  The command you want to use for this sticker is `./extract.py 3 3 0 sticker.png`
  
  Another example format:

  ```
  X  X  X  X  X
  X  X  X  X  X
  ```
 
  Then you should use: `./extract.py 5 2 0 sticker.png`

  ```
  X  X  X  X
  X  X  X  X
  X  X  X  X
  X  X  X 
  ```

  For incomplete rows, we specify the remaining tiles on the last row. `./extract.py 4 4 3 sticker.png`
  
  Use `./extract.py --help` for advanced options like resizing and adjusting the offset.

7. `$ pip install Pillow; python ./extract.py`. Done!