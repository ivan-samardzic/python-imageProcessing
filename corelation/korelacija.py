import cv2
import numpy as np
slika = cv2.imread('lena-gray.png', cv2.IMREAD_GRAYSCALE)
# Kreiranje i ispis filtera
moj_filter = np.zeros((50,50), np.float32)
moj_filter[49,0] = 1 
print(moj_filter)
# Primjena filtera na sliku
filtrirana_slika = cv2.filter2D(slika, -1, moj_filter,anchor=(-1,-1), borderType=cv2.BORDER_CONSTANT)
cv2.imwrite("Filtrirana_slika.jpg", filtrirana_slika)