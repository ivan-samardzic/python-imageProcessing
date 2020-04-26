import cv2
from PIL import Image,ImageOps
slika=Image.open('rgbPrva.jpg')
nova_slika=ImageOps.equalize(slika,mask=None)
nova_slika.save('HistSlika4zad.jpg')