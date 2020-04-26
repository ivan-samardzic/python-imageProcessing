import cv2
import numpy as np

#gamma korekcija
image = cv2.imread('lena-color.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
gamma = 0.2

corrected_image = np.power(image, gamma) 
corrected_image = corrected_image * 255 

cv2.imwrite('korekcija.jpg', corrected_image)

