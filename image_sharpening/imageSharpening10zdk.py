import cv2
import numpy as np

image = cv2.imread('lena-grayscale.jpg')
kernel = np.array([[-1,-1,-1], 
                   [-2, 16,-2],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) 
cv2.imwrite('sharpedLena10zdk.jpg',sharpened)