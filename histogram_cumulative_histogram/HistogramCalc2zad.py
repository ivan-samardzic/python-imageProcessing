import cv2
import numpy as np
slika=cv2.imread('siva_slika1zad.jpg',cv2.IMREAD_GRAYSCALE)
histogram=cv2.calcHist([slika],[0],None,[256],[0,256])
print(histogram)
cv2.imwrite('histogram.png',histogram)		