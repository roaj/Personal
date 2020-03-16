#import libraries

import numpy as np 
import cv2

#identity ONE orange ping pong ball

camera_input = 0        #define camera

#Resize parameter

size_w = 240 
size_h = 160 

#Color Range, described in HSV

class hsv:
    def __init__(self, h_min, s_min, v_min, h_max, s_max, v_max):
        self.h_min = h_min
        self.s_min = s_min
        self.v_min = v_min
        self.h_max = h_max
        self.s_max = s_max
        self.v_max = v_max

#make list of colors

red_hsv = hsv(172,124,52,186,204,255)
green_hsv = hsv(40,50,65,79,205,255)
orange_hsv = hsv(0,144,152,16,226,255)
blue_hsv = hsv(95,50,69,137,255,255)
lower = 0 
upper = 0 

def bound_giver(H_min,S_min,V_min,H_max,S_max,V_max):
        lowerb = np.array([H_min, S_min, V_min], dtype="uint8")
        upperb = np.array([H_max, S_max, V_max], dtype="uint8")
        return lowerb, upperb

while(True):
    

    #Camera input
    cam = cv2.VideoCapture(camera_input)        #Setting camera to record video

    #read frame
    ret, raw_frame = cam.read()

    #RGB to HSV
    frame_to_thresh = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2HSV)    # Otherwise continue reading in HSV

    #Perform Threshold 
    #Orange

    orange_lowerb , orange_upperb = bound_giver(orange_hsv.h_min,orange_hsv.s_min,orange_hsv.v_min,orange_hsv.h_max,orange_hsv.s_max,orange_hsv.v_max)
    thresh_orange = cv2.inRange(frame_to_thresh, orange_lowerb, orange_upperb)
    cv2.imshow("Orange_Thresh", thresh_orange)

    #Blue

    blue_lowerb , blue_upperb = bound_giver(blue_hsv.h_min, blue_hsv.s_min, blue_hsv.v_min, blue_hsv.h_max, blue_hsv.s_max, blue_hsv.v_max)
    thresh_blue = cv2.inRange(frame_to_thresh, blue_lowerb, blue_upperb)
    cv2.imshow("Orange_Thresh", thresh_blue)

    #Red

    red_lowerb , red_upperb = bound_giver(red_hsv.h_min, red_hsv.s_min, red_hsv.v_min, red_hsv.h_max, red_hsv.s_max, red_hsv.v_max)
    thresh_red = cv2.inRange(frame_to_thresh, red_lowerb, red_upperb)
    cv2.imshow("red_Thresh", thresh_red)
    
    #green

    green_lowerb , green_upperb = bound_giver(green_hsv.h_min, green_hsv.s_min, green_hsv.v_min, green_hsv.h_max, green_hsv.s_max, green_hsv.v_max)
    thresh_green = cv2.inRange(frame_to_thresh, green_lowerb, green_upperb)
    cv2.imshow("green_Thresh", thresh_green)


    ch = cv2.waitKey(1)
    if ch & 0XFF == ord('q'):
        break
cv2.destroyAllWindows()





    # lowerb,upperb = second(green_hsv)
    # print("lower = ",lowerb, "upper = ",upperb)












