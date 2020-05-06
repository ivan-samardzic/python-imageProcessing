#import modules
import cv2

#capture the video stream
cap = cv2.VideoCapture("video.avi")
#or cap = cv2.VideoCapture(0)

#to save the video
#cv2.VideoWritter arguments are output video name, fourcc code, number of frames in a sec
#width and height stream in the tuple
fourcc = cv2.VideoWritter_fourcc(*'XVID')
out = cv2.VideoWritter('output.avi',fourcc, 20.0, (640, 480))

#do it forever
while True:
    #or while(cap.isOpened()):
    
    #check ret
    if ret == True:
    
        #ret will be true or false, frame will be saved in frame variable
        ret, frame = cap.read()
        
        #print video stream widht and height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        #append the out avi with the frame object
        out.write(frame)
        
        #convert frame into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #show the video on prompt
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
        
        #check if user pressed q key every 1 ms, if it is true, vreak from while loop
        if cv2.waitKey(1) and 0xFF == ord('q')
            break
    else:
        break

#release the capture variable
cap.release()

#release the video
out.release()

#destroy all windows
cv2.destroyAllWindows()