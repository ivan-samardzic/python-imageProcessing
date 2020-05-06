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
        #create the circle with x,y center and radius = 10, red color, thickness = 3
        cv2.circle(img, (x, y), 10, (0, 0, 255), 3)
        
        #add x,y tuple coordinates into list called points
        points.append((x, y))
        
        #if the lenght of the list is greather or equal than 2, print the line and 
        #split last two spots where the usre clicked on the image, line color will be
        #green and thickness is 5
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 5)
        
        #show the image in the window
        cv2.imshow('image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
    
        #calculate each image channel indenpendently, variables will save tha color 
        #value in the image where the user clicked 
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        
        #create the circle with x,y center and radius = 10, green color, thickness = 3
        cv2.circle(img ,(x, y), 10, (0, 255, 0), 3)
        
        #create black image with 512 cols and rows 
        mycolorImage = np.zeros((512, 512), 3, uint8)
        
        #pass BGR values into new image 
        mycolorImage[:] = [blue, green, red]
        
        #show the image in the window
        cv2.imshow('color', mycolorImage)
   
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