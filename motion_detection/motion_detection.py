#modules incluede
import cv2, time, pandas
from datetime import datetime

#global object
first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

#video object creation method
video = cv2.VideoCapture(0)

#do it forever
while True:
    #check is bool data type, returns true if py is able to read the video object
    #frame is numpy array, it repesent the first image that video captures
    check, frame = video.read()
    
    #set the object
    status = 0
    
    #convert RGB frame image into grayscale with cv2 method
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #use GaussianBlur cv2 method to decrease the image noise
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    #check if fiste_frame object is empty, if it is, place gray frame in it,
    #first frame will be in that object
    if first_frame is None:
        first_frame = gray
        continue
        
    #calculate the difference between the first frame and other frames
    delta_frame = cv2.absdiff(first_frame, gray)
    
    #provide a threshold value, such that it will convert the difference value with
    #less than 30 to black, if the difference is greater than 30, it will convert to white
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations = 0)
    
    #define the contour area, basically, add the borders
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
    
    #iterate over the upperdefined area
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
            
        #change the status when the object is being detected
        status = 1
            
        #create a rectangular box around the object in the frame
        (x, y, ,w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0 , 255, 0), 3)
        
    #list of status for every frame
    status_list.append(status)
    
    status_list = status_list[-2:]
    
    #record datetime in a list when change occurs
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
        
    #show frames
    cv2.imshow("frame", frame)
    cv2.imshow("Capturing", gray)
    cv2.imshow("delta", delta_frame)
    cv2.imshow("thresh", thresh_delta)
    
    #frame will change in 1 ms
    key = cv2.waitKey(1)
    
    #check the key value, if it is q, close the for loop
    if key == ord('q'):
        break
        
#print the time
print(status_list)
print(times)

#iterate over the times object and store time values in a DataFrame
for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1], ignore_index = True)
    
#write the DataFrame to a CSV file
df.to_csv("Times.csv")

#release the video
video.release()
    
#destroy all windows
cv2.destroyAllWindows()