import numpy as np  
import cv2

img = cv2.imread("opencv-logo.png",1) #1 - default color / #0 - black and white
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img) #show img in window called "image"
#we have to tell the enviroment to take a second to display the window
#pause
cv2.waitKey(0)#command to wait a specify a time to wait, if 0 then is infinity until a key is pressed
