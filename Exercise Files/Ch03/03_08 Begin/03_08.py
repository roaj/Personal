import numpy as np
import cv2

#EDGE DETECTION
#CANNY EDGES IS A TYPE OF EDGE DETECTION ALGORITHM to help create  separation of object within the image 
#Object detection algorith look at the rate of change of color on the pixels
#canny makes a line at high contrast areas in the image 

#we want to isolate each tomato 
img = cv2.imread("tomatoes.jpg",1)
#we are going to do a threshold to see that it does not work 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#theshold using only hue channel
res, thresh = cv2. threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresh", thresh)
#threshold did not work propely, it got part of the background and may look like one thing

edges = cv2.Canny(img,100,70)
cv2.imshow("Canny",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()