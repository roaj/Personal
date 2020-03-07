#Getting Started with open cv
import cv2
import numpy as np 

img = cv2.imread("opencv-logo.png") #read in image we have to be in the same folder as the image
cv2.namedWindow("image",cv2.WINDOW_NORMAL)#display our image using a window / 0 for default behaivor or cv2.WINDOW_NORMAL / initialize the window that will be used to show the image 
cv.2imshow("image",img) #show img in window called "image"
#we have to tell the enviroment to take a second to display the window
#pause
cv2.waitKey(0)#command to wait a specify a time to wait, if 0 then is infinity until a key is pressed

