#import modules
import cv2
import numpy as np

#empty method to pass it to tracker
def noothing(x):
    pass
    
#capture video frame
    
#create track bars
cv2.namedWindow("Tracking")
cv2.createTrackbar("lower hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("lower saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("lower value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("upper hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("upper saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("upper value", "Tracking", 255, 255, nothing)

#do it forever
while True:
    #take a frame
    #frame = cv2.imread("lena.jpg")
    
    #in frame read video
    -, frame = cap.read()
     
    #convert it to HSV
    hsv = cv2.cvtColor(frame, COLOR_BGR2HSV)
    
    #make trackers for bars
    l_h = cv2.getTrackbarPos("lower hue", "Tracking")
    l_s = cv2.getTrackbarPos("lower saturation", "Tracking")
    l_v = cv2.getTrackbarPos("lower value", "Tracking")
    u_h = cv2.getTrackbarPos("upper hue", "Tracking")
    u_s = cv2.getTrackbarPos("upper saturation", "Tracking")
    u_v = cv2.getTrackbarPos("upper value", "Tracking")
    
    #create an array from upper values
    l_b = np.array([l_h,l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    #create a mask to and it with the frame image
    mask = cv2.inRange(hsv, l_b, u_b)
    
    #make bit_and operation
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    #show frame, mask and result image
    cv2.imshow('lena', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)
    
    #wait user to press any key, scan the keyboard every 1ms, if the user pressed 27,
    #break from the loop
    key = cv2.waitKey(1)
    if key == 27:
        break
        
#release the video
cap.release()

#destroy all windows
cv2.destroyAllWindows()