#importing Libraries
import numpy as np
import cv2

#Camera
#Original Frame size 
    #(480,640,3) RGB
camera_input = 0    #define camera imput

size_w = 240 #resize image width
size_h = 160 #resize image height 

#RGB or HSV

filter = 'HSV'

camera = cv2.VideoCapture(camera_input) #Define camera
camera.set(3, size_w) #Overriding width of frame
camera.set(3, size_h)  #Overriding height of fram

while(True):

    ret,image = camera.read()       #Read frame calling it image
    



    cv2.imshow("Image",image)
    print(image.shape)

    ch = cv2.waitKey(1) #run every 1 milisecond / if 10 then would wait 10 miliseconds
    if ch & 0xFF == ord('q'): #if not 64 bibt pc then if ch == ord('q)
        break

camera.release()
cv2.destroyAllWindows()



