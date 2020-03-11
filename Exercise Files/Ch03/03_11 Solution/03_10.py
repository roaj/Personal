import numpy as np
import cv2
import random

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original",img)

#Convert image to grascale to perform thresholding
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur as a trick to help the adaptive threshold
blur = cv2.GaussianBlur(gray, (3,3),0)
#make the adaptive Threshold 
#Selecting binary_inverse because of the foreground of the image was white
# and we want to take out the objects which will be darker in this color
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Binary",thresh)

#Lets get the contours 
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours)) #initially there is a lot because of the little areas becuase of the basic filtering

#filter that image by doing the area. check all the contours and then just add to the 
#filtered array the contours that are big enough 
filtered = []
for c in contours:
	if cv2.contourArea(c) < 1000:continue
	filtered.append(c)

#From 2054 we went to 4
#
print(len(filtered))

#now lets draw our contours 

#blank image
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in filtered:
	#random for picking colors (ranodom.randint(0,255), same, same) as BGR
	col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	#draw filtered contours. They will be filled. its like drawing the image all over on top of the foreground
	cv2.drawContours(objects,[c], -1, col, -1)
	area = cv2.contourArea(c)
	p = cv2.arcLength(c,True)
	print(area,p)# printing area and perimeter

cv2.imshow("Contours",objects)
	

cv2.waitKey(0)
cv2.destroyAllWindows()