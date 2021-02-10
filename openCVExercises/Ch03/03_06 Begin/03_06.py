#commented
import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
#Use the image as a grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#make a threshold 
#transforms a grayscale image into a binary image according to the setup
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("binary",thresh)

#Setting up our contours command
#it has three outputs
#first one: we dont care
#second (contour) : the list individual contrours / each contour is a list of points which describe a parameter of an object
#third ( hierarchy) : parent child relationship of all the contours (who encloses who)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#make a copy of original image
img2 = img.copy()
#index of a contour we want to draw / -1 : will draw all contours 
index = -1
#thickness of contour
thickness = 4
#color of contour BGR
color = (255, 0, 255)

#draw contour
cv2.drawContours(img2, contours, index,color,thickness)
cv2.imshow("contour",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()