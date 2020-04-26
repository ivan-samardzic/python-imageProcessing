import cv2
import numpy as np

#slika = cv2.imread('lena-grayscale.jpg')
#slika2 = cv2.imread('slika_1.jpg')

#retci = slika.shape[0]
#stupci = slika.shape[1]
#kanali = slika.shape[2]

#for k in range(0, kanali):
    #for i in range(0, retci):
        #for j in range(0, stupci):
            #m = 0
            #niz = []
            #for z in range(i-1, i+1):
                #for l in range(j-1, j+1):
                    #niz.append(slika[i,j,k])
                    #niz_sort = niz.sort
                    #m = niz_sort(4)
        #slika2[i,j,k] = m


#cv2.imwrite("Filtrirana slika_2.jpg", slika2)

img = cv2.imread('lena-grayscale.jpg')
median = cv2.medianBlur(img, 5)
cv2.imwrite("median.jpg", median)