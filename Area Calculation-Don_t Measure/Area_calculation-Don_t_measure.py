"""
@author: Arpit Somani
"""

from PIL import Image
import random

im=Image.open("map1.png")
rgb_im=im.convert("RGB")

count_pun=0
count_in=0
count=0

while(count<=100000):
    x=random.randint(0,180)
    y=random.randint(0, 180)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==195):
        count_in=count_in+1
        count=count+1
    else:
        if(r==237):
            count_pun=count_pun+1
            count=count+1
        
area_pun=(count_pun/count_in)*3287263
print(area_pun)