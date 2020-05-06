#include modules
import numpy as np
import cv2

#import the real image
img = cv2.imread('messi.jpg')
 
#returns a tuple od number of rows, cols and channels
print(img.shape)

#returns total number od pixels is accessed
print(img.size)

#returns image datatype is obtained
print(img.dtype)

#split RGB image into 3 channels
b, g, r = cv2.split(img)

#make the reverse method and split the channels
img = cv2.merge((b, g, r))

#putting ROI into ball variable
ball = img[280:340, 330:390]

#adding the ball at the different place in the image
img[273:333, 100:160] = ball

#show RGB image and each channel separetly
cv2.imshow('image', img)
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)