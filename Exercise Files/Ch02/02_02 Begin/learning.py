import numpy as np  
import cv2

img = cv2.imread("opencv-logo.png",1) #1 - default color / #0 - black and white
img.shape #telling us the # of rows , # of columns, # channels
img.dtype #find data type of image uint8 = mac of 2^8= 256 in each pixel => range of values is from 0 to 255
img[:,:,0] #values of the first channel
img.size #find total number of pixels
