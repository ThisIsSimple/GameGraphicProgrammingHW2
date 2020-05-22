# Convert image to binary data 

### 1. Use Image Magick

Image Magick help us to read image file as binary data.

[Download Image Magick](https://imagemagick.org/script/download.php)

magick down_pusheen.png out.h

Result File "out.h"

### 2. Convert Binary Data To Texel Data

Use Python Code to do that.

Put binary data in "data.py"
"main.py" read data.py and split data into texel type data

Result File "converted.txt"

### 3. Create Texture Header File

Code Texture Header File with converted data.

Result File "pusheen.h"