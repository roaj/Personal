class hsv:
    def __init__(self, h_min, s_min, v_min, h_max, s_max, v_max):
        self.h_min = h_min
        self.s_min = s_min
        self.v_min = v_min
        self.h_max = h_max
        self.s_max = s_max
        self.v_max = v_max

#make list of colors

colors = (red, green)
red_hsv = hsv(172,124,52,186,204,255)
green_hsv = hsv(40,50,65,79,205,255)
orange_hsv = hsv(0,144,152,16,226,255)
blue_hsv = hsv(95,50,69,137,255,255)

#Camera input
  # Otherwise continue reading in HSV

#Perform Threshold 
for color in colors:
    test = color + ("_hsv.h_min") 
    print(test)




# orange_lowerb , orange_upperb = bound_giver(orange_hsv.h_min,orange_hsv.s_min,orange_hsv.v_min,orange_hsv.h_max,orange_hsv.s_max,orange_hsv.v_max)
# thresh_orange = cv2.inRange(frame_to_thresh, orange_lowerb, orange_upperb)
# cv2.imshow("Orange_Thresh", thresh_orange)
