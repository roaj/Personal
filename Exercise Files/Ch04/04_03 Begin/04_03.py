import numpy as np
import cv2

#Template Matching
#A way to detect features in an image
    #works by sliding a soure template image and making a difference at every location 
    #againt a reference image and determine how close those images are together 
    #if there is matching the result image will seem with a bight spot

#reading as a grayScale
template = cv2.imread('template.jpg',0)
frame = cv2.imread("players.jpg",0)
#display
cv2.imshow("Frame", frame)
cv2.imshow("Template",template)
#perform the matching / one of several methods of doing matching 
result = cv2.matchTemplate(frame,template, cv2.TM_CCOEFF_NORMED)

#where is that location 
#getting the maximun britghness out of the resultan image
min_val, max_val, min_loc,max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)
cv2.circle(result,max_loc,20,255,2)
#show result 
cv2.imshow("Matching",result)

cv2.waitKey(0)
cv2.destroyAllWindows(x)