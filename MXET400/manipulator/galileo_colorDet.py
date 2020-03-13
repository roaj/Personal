#importing Libraries
import numpy as np
import cv2

#Camera
#Original Frame size 
    #(480,640,3) RGB
camera_input = 0    #define camera imput

size_w = 240 #resize image width
size_h = 160 #resize image height 

#    Color Range, described in HSV

v1_min = 10     # Minimum H value
v2_min = 150    # Minimum S value
v3_min = 50    # Minimum V value

v1_max = 20     # Maximum H value
v2_max = 255     # Maximum S value
v3_max = 255    # Maximum V value


#RGB or HSV

filter = 'HSV'

camera = cv2.VideoCapture(camera_input) #Define camera
#camera.set(3, size_w) #Overriding width of frame
#camera.set(4, size_h)  #Overriding height of fram
x = 0  # will describe target location left to right
y = 0  # will describe target location bottom to top
radius = 0  # estimates the radius of the detected target

while(True):

    ret,image = camera.read()       #Read frame calling it image
    height, width, channels = image.shape


    if not ret:
        break

    if filter == 'RGB':                     # If image mode is RGB switch to RGB mode
        frame_to_thresh = image.copy()
    else:
        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    # Otherwise continue reading in HSV

    thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))   # Find all pixels in color range

    kernel = np.ones((5,5),np.uint8)                            # Set gaussian blur strength.
    mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)     # Apply gaussian blur
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]     # Find closed shapes in image
    # center = None   # Create variable to store point


    cv2.imshow("Image",image)
    cv2.imshow("mask",thresh)
    print(image.shape)

    ch = cv2.waitKey(1) #run every 1 milisecond / if 10 then would wait 10 miliseconds
    if ch & 0xFF == ord('q'): #if not 64 bibt pc then if ch == ord('q)
        break

camera.release()
cv2.destroyAllWindows()



