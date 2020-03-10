import cv2
import numpy as np 

color = cv2.imread("buttefly.jpg",1)

#convert to grayscale
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY) #RGBBGR
cv2.imwrite("gray.jpg",gray)

#setup alpha channel
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite("rgbba.png",rgba)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
