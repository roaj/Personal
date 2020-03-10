import numpy as np
import cv2

img = cv2.imread('faces.jpg',1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v),axis=1)
cv2.imshow("hsv split", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()