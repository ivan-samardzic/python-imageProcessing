import cv2
import numpy as np
image_gray = cv2.imread('jimi.jpg', cv2.IMREAD_GRAYSCALE)
(prag, binary_image) = cv2.threshold(image_gray, 127, 255,cv2.THRESH_BINARY)
myfilter = np.ones((5,5), np.uint8)
image = cv2.dilate(binary_image, myfilter, iterations= 1)
image = cv2.erode(binary_image,myfilter, iterations = 1)
cv2.imwrite('Closing_image13zdk.jpg', image)