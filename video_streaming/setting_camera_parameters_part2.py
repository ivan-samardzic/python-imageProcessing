#include modules
import cv2
import datetime

#capture the video stream and save it into cap variable
cap = cv2.VideoCapture(0)

#print on the prompt video stream height and width
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#set the dimensions and print it on the prompt
cap.set(3, 3000)
cap.set(4, 4000)
#print(cap.get(3))
#print(cap.get(4))

#while video from camera is captured
while(cap.isOpened()):

    #read the video from cam and in ret variable save boolean value is the video captured
    #in frame variable save the first stream captured
    ret, frame = cap.read()
    
    #check if boolean value is true
    if ret == True:
    
        #define the font, select the date and create string text, add it to the frame
        #show frame on the window
        font = cv2.FONT_HERSHEY_SIMPLEX
        date_time = str(datetime.datetime.now())
        text = 'Width: ' + str(cap.get(3)) + ' ' + 'height: ' + str(cap.get(4)) + '\n' + date_time
        frame = cv2.putText(frame, text, (10, 50), font, 3, (255, 255, 0), 10, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        #check if user pressed q key and if it is true break from the loop
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    else:
        break
        
#release captured video 
cap.release()

#destroy all windows
cv2.destroyAllWindows()