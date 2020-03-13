#importing Libraries
import numpy as np
import cv2

#Camera

camera_input = 0    #define camera imput

size_w = 240 #resize image width
size_h = 160 #resize image height 

#RGB or HSV

filter = 'HSV'

camera = cv2.VideoCapture(camera_input) #Define camera

while(True):

    ret,image = camera.read()
    cv2.imshow("Image",image)
    print(image.shape)

    ch = cv2.waitKey(1) #run every 1 milisecond / if 10 then would wait 10 miliseconds
    if ch & 0xFF == ord('q'): #if not 64 bibt pc then if ch == ord('q)
        break

camera.release()
cv2.destroyAllWindows()



