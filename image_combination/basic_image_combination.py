#include modules
import numpy as np
import cv2

#import the real image
img = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv-logo.png')
 
#returns a tuple od number of rows, cols and channels
print(img.shape)
print(img2.shape)

#returns total number od pixels is accessed
print(img.size)
print(img2.size)

#returns image datatype is obtained
print(img.dtype)
print(img2.dtype)

#split RGB image into 3 channels
b, g, r = cv2.split(img)

#make the reverse method and split the channels
img = cv2.merge((b, g, r))

#putting ROI into ball variable
ball = img[280:340, 330:390]

#resize two images to have the same size, it can not be added together if the dimesions 
#are not equal
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#adding two images together
img_dst = cv2.add(img, img2)

#adding two images together with different method
#img will be dominant with 90 percent, img2 will be reccesive with 10 percent
#gamma factor is 0
#img_dst = cv2.addWeighted(img, .9, img2, .1, 0)


#adding the ball at the different place in the image
img[273:333, 100:160] = ball

#show RGB image and each channel separetly
cv2.imshow('image', img)
cv2.imshow('image', img_dst)
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)