#transform to different colors

import numpy as np 
import cv2

color = cv2.imread("butterfly.jpg",1) #load the image as defaul (1)
cv2.imshow("Image",color) #display image 
cv2.moveWindow("Image",0,0) # put image on top left corner
print(color.shape) #give us 3 parameters meaning the image has 356 pixels tall, 493 pixel wide and it has 3 color channels
height,width,channels = color.shape #[356,493,3]

b,g,r = cv2.split(color) #will split our channels of the color image into each of its components as an individual matrix

rgb_split = np.empty([height,width*3,3],'uint8')

rgb_split[:,0:width] = cv2.merge ([b,b,b])
rgb_split[:,width:width*2] = cv2.merge([g,g,g])
rgb_split[:,width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("channels",rgb_split)
cv2.moveWindow("channel",0,height)

hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV) #convertio between BGR and HSV
h,s,v = cv2.split(hsv) 
hsv_split=np.concatenate((h,s,v),axis=1) #concatinate this channels that were just created
cv2.imshow("HSV",hsv)
cv2.imshow("split_HSV", hsv_split)
#Hue =is the color portion of the model, expressed as a number from 0 to 360 degrees: Red falls between 0 and 60 degrees. Yellow falls between 61 and 120 degrees. Green falls between 121-180 degrees
#saturation = Saturation describes the amount of gray in a particular color, from 0 to 100 percent. Reducing this component toward zero introduces more gray and produces a faded effect.
#value = Value works in conjunction with saturation and describes the brightness or intensity of the color, from 0-100 percent, where 0 is completely black, and 100 is the brightest and reveals the most color.

cv2.waitKey(0)
cv2.destroyAllWindows()
