import cv2
import numpy as np

image=cv2.imread('rgbPrva.jpg')
LaplacesKernel=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
detectedEdge=cv2.filter2D(image,-1,LaplacesKernel)
cv2.imwrite('detectedImage11azdk.jpg',detectedEdge)