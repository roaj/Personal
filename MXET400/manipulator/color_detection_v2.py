#Import necessary libraries
import cv2
import time
import numpy as np

#make class for handling hsv
class hsv:
    def __init__(self, h_min, s_min, v_min, h_max, s_max, v_max, flag):
        self.h_min = h_min
        self.s_min = s_min
        self.v_min = v_min
        self.h_max = h_max
        self.s_max = s_max
        self.v_max = v_max
        self.flag = flag

#declare hsv bounds
red_hsv = hsv(172,124,52,186,204,255,0)
green_hsv = hsv(40,50,65,79,205,255,0)
orange_hsv = hsv(0,144,152,16,226,255,0)
blue_hsv = hsv(95,50,69,137,255,255,0)

#gipper flag
gripper_flag = 0 #begin open 


def nothing(n):
    pass

#finding the index of the biggest contour
def biggestContourI(contours):
    maxVal = 0
    maxI = None
    for i in range(0, len(contours) - 1):
        if len(contours[i]) > maxVal:
            cs = contours[i]
            maxVal = len(contours[i])
            maxI = i
    return maxI

#re-assign bounds
def bound_giver(H_min,S_min,V_min,H_max,S_max,V_max):
        lowerb = np.array([H_min, S_min, V_min], dtype="uint8")
        upperb = np.array([H_max, S_max, V_max], dtype="uint8")
        return lowerb, upperb



def color_detection():

    #use usb camera
    cam = cv2.VideoCapture(0)

    red_hsv.flag = 0
    green_hsv.flag = 0 
    orange_hsv.flag = 0
    blue_hsv.flag = 0

    ret, img = cam.read()
    h, w = img.shape[:2]

    #RED

    #get lower and upper boundary 
    red_lowerb , red_upperb = bound_giver(red_hsv.h_min, red_hsv.s_min, red_hsv.v_min, red_hsv.h_max, red_hsv.s_max, red_hsv.v_max)
    #basic Threshold
    frame_to_thresh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh_red = cv2.inRange(frame_to_thresh, red_lowerb, red_upperb)
    #Contours
    contours_red, hierarchy = cv2.findContours(thresh_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find the biggest contour / returns the index
    bc = biggestContourI(contours_red)
    #when no contour found the return value is None and fucks up the program soooo..
    if bc == None:
        pass
    elif bc >= 0:
            #find Area of biggest contour
        big_contour_area = cv2.contourArea(contours_red[bc])
        if big_contour_area > 100000:
            #print ("Item Area = {}".format(big_contour_area))
            red_hsv.flag = 1
            cv2.drawContours(img,contours_red, bc, (0,0,255), 3)


    #BLUE

    #get lower and upper boundary 
    blue_lowerb , blue_upperb = bound_giver(blue_hsv.h_min, blue_hsv.s_min, blue_hsv.v_min, blue_hsv.h_max, blue_hsv.s_max, blue_hsv.v_max)
    #basic Threshold
    frame_to_thresh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh_blue = cv2.inRange(frame_to_thresh, blue_lowerb, blue_upperb)
    #Contours
    contours_blue, hierarchy = cv2.findContours(thresh_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find the biggest contour / returns the index
    bc = biggestContourI(contours_blue)
    #when no contour found the return value is None and fucks up the program soooo..
    if bc == None:
        pass
    elif bc >= 0:
            #find Area of biggest contour
        big_contour_area = cv2.contourArea(contours_blue[bc])
        if big_contour_area > 100000:
            #print ("Item Area = {}".format(big_contour_area))
            blue_hsv.flag = 1
            cv2.drawContours(img,contours_blue, bc, (255,0,0), 3)



    #GREEN

    #get lower and upper boundary 
    green_lowerb , green_upperb = bound_giver(green_hsv.h_min, green_hsv.s_min, green_hsv.v_min, green_hsv.h_max, green_hsv.s_max, green_hsv.v_max)
    #basic Threshold
    frame_to_thresh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh_green = cv2.inRange(frame_to_thresh, green_lowerb, green_upperb)
    #Contours
    contours_green, hierarchy = cv2.findContours(thresh_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find the biggest contour / returns the index
    bc = biggestContourI(contours_green)
    #when no contour found the return value is None and fucks up the program soooo..
    if bc == None:
        pass
    elif bc >= 0:
            #find Area of biggest contour
        big_contour_area = cv2.contourArea(contours_green[bc])
        if big_contour_area > 100000:
            #print ("Item Area = {}".format(big_contour_area))
            green_hsv.flag = 1
            cv2.drawContours(img,contours_green, bc, (0,255,0), 3)

    #ORANGE

    #get lower and upper boundary 
    orange_lowerb , orange_upperb = bound_giver(orange_hsv.h_min, orange_hsv.s_min, orange_hsv.v_min, orange_hsv.h_max, orange_hsv.s_max, orange_hsv.v_max)
    #basic Threshold
    frame_to_thresh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh_orange = cv2.inRange(frame_to_thresh, orange_lowerb, orange_upperb)
    #Contours
    contours_orange, hierarchy = cv2.findContours(thresh_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #find the biggest contour / returns the index
    bc = biggestContourI(contours_orange)
    #when no contour found the return value is None and fucks up the program soooo..
    if bc == None:
        pass
    elif bc >= 0:
            #find Area of biggest contour
        big_contour_area = cv2.contourArea(contours_orange[bc])
        if big_contour_area > 100000:
            #print ("Item Area = {}".format(big_contour_area))
            orange_hsv.flag = 1
            cv2.drawContours(img,contours_orange, bc, (0,255,0), 3)
    #
    #Check FLAGS

    if red_hsv.flag == 1:
        print("Red golf ball detected")
        #return red_hsv.flag
    elif green_hsv.flag == 1:
        print("Green golf ball detected")
        #return green_hsv.flag
    elif orange_hsv.flag == 1:
        print("Orange golf ball detected")
    elif blue_hsv.flag == 1:
        print("Blue golf ball detected")
    else:
        print("no golf ball detected")
    



def move_servo():
    pass



print(green_hsv.flag)
time.sleep(3)
print("going now")
color_detection() #update Flag of color
print(green_hsv.flag)
time.sleep(2)
color_detection()
print(green_hsv.flag)

cv2.destroyAllWindows()