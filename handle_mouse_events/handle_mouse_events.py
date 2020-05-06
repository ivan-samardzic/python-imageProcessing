#include modules
import numpy as np
import cv2

#print all the events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

#define mouse click event method
def click_event(event, x, y, flags, param):

    #check if user pressed left mouse button
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #print x and y coordinates
        print(x, ',',  y)
        
        #define font and text variable
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + "," + str(y)
        
        #add text to the image
        cv2.putText(img, text, (x, y), font, 1, (255, 255, 0), 2)
        
        #show the image in the window
        cv2.imshow('image', img)
    
    #check if user pressed left mouse button
    if event == cv2.EVENT_RBUTTONDOWN:
    
        #calculate each image channel indenpendently
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        
        #define font and text variable
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + "," + str(green) + "," + str(red)
        
        #add text to the image
        cv2.putText(img, text, (x, y), font, 1, (0, 255, 255), 2)
        
        #show the image in the window
        cv2.imshow('image', img)
   
#create np zeros array with 512 cols and rows, 3 channels, datatype uint8
#img = np.zeros((512, 512), 3, np.uint8)

#import the real image
img = cv2.imread('lena.jpg')

#show the image in the window
cv2.imshow('image', img)

#call the setMouseCallback method 
cv2.setMouseCallback('image', click_event)

#wait the user to press any key 
cv2.waitKey(0)

#destroy all windows
cv2.destroyAllWindows()    

