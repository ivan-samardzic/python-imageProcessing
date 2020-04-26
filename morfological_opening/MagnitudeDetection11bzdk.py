import cv2
import numpy as np

image=cv2.imread('rgbPrva.jpg')
kernel1=np.array([[-1,0,1],[-2,0,-2],[-1,0,-1]])
kernel2=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
kernel=np.ones((3,3))
for i in range(0,2):
	for j in range(0,2):
		kernel=kernel1(i,j)+kernel2(i,j)
filter_image=cv2.filter2D(image,-1,kernel)
cv2.imwrite('filterImage11bzdk.jpg',filter_image)