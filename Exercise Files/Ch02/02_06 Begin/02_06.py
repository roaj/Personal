import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
cv2.imshow("original",image)

#Bluring an Image
blur = cv2.GaussianBlur(image,(5,55),0) #blurr a bit on x but a lot on y
cv2.imshow("Blur",blur)


#dilation and Erosion 
#dilation - turn black pixels or background pixels into white pixels
#Erosion - turns white pixels into black pixels, 

Kernel = np.ones((5,5),'uint8') #the thing that goes through every pixel
dilate = cv2.dilate(image,Kernel,iterations=1) #each iteration will eat more
erode = cv2.erode(image,Kernel, iterations=1)

cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)





cv2.waitKey(0)
cv2.destroyAllWindows()