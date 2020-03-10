import numpy as np  
import cv2

cap = cv2.VideoCapture(0) #continous 

while(True):

    ret, frame = cap.read() #read from the video stream 
    #resize
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # (0,0) means not telling it how many pixels should it have but rather by percentage
    cv2.imshow("frame",frame)

 
    ch = cv2.waitKey(1) #run every 1 milisecond / if 10 then would wait 10 miliseconds
    if ch & 0xFF == ord('q'): #if not 64 bibt pc then if ch == ord('q)
        break


cap.release()
cv2.destroyAllWindows()
