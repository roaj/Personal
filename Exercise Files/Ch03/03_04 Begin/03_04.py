import numpy as np
import cv2

image = cv2.imread('faces.jpg',1)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
#keeping all the oroginal pixels but just one channel h , s , v
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]
#put all those hsv channels next to each other on the same tab
#axis=1 to be horizontal
hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv split", hsv_split)
#to convine to filters irs very usefull sometime
#specially for further image processing tasks

#apply threshold filter to the saturation channels
#Everything on this channel that has a value of LESS THAN 40 WILL APPEAR AS WHITE
ret, thresh_1 = cv2.threshold(s,40,244,cv2.THRESH_BINARY)
cv2.imshow("Sat_Filter",thresh_1)
#Do the same for the HUE CHANNEL
#inverse of the normal order of the threshold
#WILL MAKE VALUES FROM 0 TO 15 WHITE
ret, thresh_2 = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV) 
cv2.imshow("Hue Filter",thresh_2)

#combine filters together
final = cv2.bitwise_and(thresh_1,thresh_2)
cv2.imshow("Final",final)



cv2.waitKey(0)
cv2.destroyAllWindows()