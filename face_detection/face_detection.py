#include modules
import cv2

#create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#reading the image as it is
img = cv2.imread("photo.jpg")

#reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

#iterate over the image
for x,y,w,h in faces:
    image = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 3)
    
#resize the image
resized = cv2.resize(img, (int(img.shape[1] / 7), int(img.shape[0] / 7)))

#save new image 
cv2.imwrite("new_photo.jpg", resized)