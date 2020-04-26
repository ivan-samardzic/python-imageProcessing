import cv2
import numpy as np
image_gray = cv2.imread('jimi.jpg', cv2.IMREAD_GRAYSCALE)
(prag, binary_image) = cv2.threshold(image_gray, 127, 255,cv2.THRESH_BINARY)
myfilter = np.ones((5,5), np.uint8)
erosion_image = cv2.erode(binary_image,myfilter, iterations = 1)
dilatation_image = cv2.dilate(binary_image, myfilter, iterations= 1)
cv2.imwrite('Siva slika13zdk.jpg', image_gray)
cv2.imwrite('Binarna slika13zdk.jpg', binary_image)
cv2.imwrite('Erozija13zdk.jpg', erosion_image)
cv2.imwrite('Dilatacija13zdk.jpg', dilatation_image)