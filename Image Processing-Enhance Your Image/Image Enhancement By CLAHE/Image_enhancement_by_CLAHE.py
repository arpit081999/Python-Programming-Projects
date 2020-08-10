"""
@author: Arpit Somani
"""

#image enhancement CLAHE
import cv2
#read the image
img=cv2.imread("crime.jpg")
#prepartion to CLAHE
clahe=cv2.createCLAHE()
#convert to gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply enhancement
enh_img=clahe.apply(gray_img)
#save it to a file
cv2.imwrite("enhanced.jpg",enh_img)
print("Done Enhancing")
