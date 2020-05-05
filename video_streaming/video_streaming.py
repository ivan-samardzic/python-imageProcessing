#modules incluede
import cv2, time

#video object creation method
video = cv2.VideoCapture(0)

#declare and initilise a variable
a = 1

#do it forever
while True:

    #increment the variable
    a += 1
    
    #check is bool data type, returns true if py is able to read the video object
    #frame is numpy array, it repesent the first image that video captures
    check, frame = video.read()
    print(frame)
    
    #RGB frame conversion int grayscale image
    gray = cv2.cvtColor(frame, cv2.COLORBGR2GRAY)
    
    #showing grayscale image at the screen
    cv2.imshow("Capturing", gray)
    
    #for 1 ms there will be new frame
    key = cv2.waitKey(1)
    
    #when the user press q, all terminates
    if key == ord('q'):
        break

#this will print the number of frames       
print(a) 
video.release()
cv2.destroyAllWindows()