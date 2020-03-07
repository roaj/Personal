import cv2
import numpy as np  

black = np.zeros([150,200,1],'uint8')#creates an array of zeros / firt imput is the size or shape [raw,colum,channel] / second input is the type of image 'uint8' /
cv2.imshow("Black",black)
print(black[0,0,:])#we loop at the first pixel 0,0 : to see all the values at that location

ones = np.ones([150,200,3],'uint8') #
cv2.imshow("ones",ones)
print(ones[0,0,:])

white = np.ones([150,200,3],'uint16')
white *= (2**16-1) #multiply every element on the array
cv2.imshow("white",white) #make a window called white and put the picture white on it
print(white[0,0,:]) #print the value of the pixel 

color = ones.copy() #make a ccopy of line 12 
color[:,:,:] = (255,0,0) # make every element blue , BGR order 
cv2.imshow("color",color) 
print(color[0,0,:]) 

cv2.waitKey(0) #wait until key is inputed 
cv2.destroyAllWindows() #clean up, close every window

#. <( wget -O - https://code.headmelted.com/installers/apt.sh )