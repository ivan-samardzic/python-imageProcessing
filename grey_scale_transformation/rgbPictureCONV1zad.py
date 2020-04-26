import cv2
slika_u_boji=cv2.imread('rgbPrva.jpg')
slika_siva=cv2.cvtColor(slika_u_boji,cv2.COLOR_BGR2GRAY)
cv2.imwrite('siva_slika1zad.jpg',slika_siva)