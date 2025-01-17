# main.py

from PIL import Image, ImageFilter, ImageDraw, ImageFont 
import os, sys
import requests
from io import BytesIO
from FunctionsPackage.Functions import *


if __name__ == "__main__":
 
#RELATIVE Path - can exchange code and it will still work on different machines
    im = Image.open(r"..\ImageArchivePackage\ImageArchive\Nippert.jpg")   #File has to be relative to the entry point
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image

# if it starts with '..' its relative, if its absolute is starts with 'C:'

    # Indenting to show code is part of above if statement
    my_image = load_image(r"..\ImageArchivePackage\ImageArchive\Nippert.jpg")
    my_image.show(my_image)
# Python is intuitive enough to open the Windows Photo Viewer
# We created a temporary image file by running thousands of lines of code using the .show



