import cv2
from PIL import Image,ImageOps
slika=Image.open('rgbPrva.jpg')
auto_con=ImageOps.autocontrast(slika,cutoff=0)
auto_con.save('konstast_slika.jpg')