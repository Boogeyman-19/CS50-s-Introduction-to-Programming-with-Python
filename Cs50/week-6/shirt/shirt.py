import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input.jpg output.jpg")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not (input_filename.lower().endswith(('.jpg', '.jpeg', '.png')) and output_filename.lower().endswith(('.jpg', '.jpeg', '.png'))):
    sys.exit("Error: File must be a JPEG or PNG")

if os.path.splitext(input_filename)[1] != os.path.splitext(output_filename)[1]:
    sys.exit("Error: Input and output files must have the same extension")

try:
    with Image.open(input_filename) as img:
        shirt = Image.open("shirt.png")
        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, (0, 0), shirt)
        img.save(output_filename)
except FileNotFoundError:
    sys.exit("Error: Input file not found")
