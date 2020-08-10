"""
@author: Arpit Somani
"""

#flipping the image
from PIL import Image
#opening the image
img=Image.open("obtained.png")
#transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
#SAVE IT TO A FILE IN A HUMAN UNDERSTANDABLE FORMET
transposed_img.save("corrected.png")
print("Done Flipping")
