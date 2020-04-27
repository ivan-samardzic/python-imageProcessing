import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('albert_grey.jpg')
edges = cv.Canny(img,100,200)
cv.imwrite('albert_grey_edge.jpg',edges)