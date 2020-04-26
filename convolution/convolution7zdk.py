import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('bbKing.jpg')
kernel=np.ones((5,5),np.float32)/25
kernel[4,3]=4
imgNew=cv2.filter2D(img,-1,kernel)
cv2.imwrite('convolutionImage7.jpg',imgNew)