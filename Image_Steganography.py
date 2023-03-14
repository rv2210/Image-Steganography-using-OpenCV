from turtle import end_fill
import cv2 as cv
import sys
from matplotlib import pyplot as plt
import numpy as np

default_image= cv.imread('C:/Users/vegesna/Documents/Opencv/Generated_Images/for_watson.png')
#plt.imshow(default_image)
#plt.show()
## When the image is read using imread or video capture in opencv2 it is read in BGR format so note this
default_image= default_image [:,:,::-1] #Reads from back converting BGR to RGB
#plt.imshow(default_image)
#plt.show()
print(default_image.shape)

blank_image= np.zeros((480,640,3), dtype='uint8')
#plt.imshow(blank_image)
#plt.show()
#k= default_image[180,180]
#print(k)
for i in range (0,160):
    for j in range (0,640):
        k= default_image[i,j]
        kr=k[0]
        kg=k[1]
        kb=k[2]
        if kr>0 or kg>0 or kb<255:
            blank_image[i,j]= [255,255,255]
        else:
            pass
for i in range (160,320):
    for j in range (0,640):
        k= default_image[i,j]
        kr=k[0]
        kg=k[1]
        kb=k[2]
        if kr>0 or kg<255 or kb>0:
            blank_image[i,j]= [255,255,255]
        else:
            pass
for i in range (320,480):
    for j in range (0,640):
        k= default_image[i,j]
        kr=k[0]
        kg=k[1]
        kb=k[2]
        if kr<255 or kg>0 or kb>0:
            blank_image[i,j]= [255,255,255]
        else:
            pass        
plt.imshow(blank_image)
plt.show() 
