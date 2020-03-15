import numpy as np 
import cv2

#identity ONE orange ping pong ball

camera_input = 0        #define camera

#Resize parameter
size_w = 240 
size_h = 160 

#Color Range, described in HSV
#HSV Values for color Detection ([v1_min, v2_min, v3_min],[v1_max, v2_max, v3_max])
red_hsv = (172,124,52,186,204,255)
green_hsv = (40,50,65,79,205,255)
orange_hsv = (0,144,152,16,226,255)
lower = 0 
upper = 0 

#Camera input
cam = cv2.VideoCapture(camera_input)        #Setting camera to record video
ret, raw_frame = cam.read()         #Reading raw_frame from camera

#Let's Check for color 

def main():

    #Camera input
    cam = cv2.VideoCapture(camera_input)        #Setting camera to record video
    cam.set(3,size_w)
    cam.set(4,size_h)

    #read frame
    ret, raw_frame = cam.read()

    #RGB to HSV
    frame_to_thresh = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2HSV)    # Otherwise continue reading in HSV

    #Perform Threshold with orange
    orange_lowerb , orange_upperb = bound_giver(orange_hsv)
    thresh_orange = cv2.inRange(frame_to_thresh, orange_lowerb, orange_upperb)
    cv2.imshow("Orange_Thresh", thresh_orange)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


def bound_giver(H_min,S_min,V_min,H_max,S_max,V_max):
    lowerb = np.array([H_min, S_min, V_min], dtype="uint8")
    upperb = np.array([H_max, S_max, V_max], dtype="uint8")
    mask = cv2.inRange()
    return(lower, upper)









