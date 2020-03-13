import cv2
import numpy as np

def nothing(x):
    pass

#setting up camera
#img = np.zeros((300,512,3), np.uint8)
cam = cv2.VideoCapture(0)
size_w = 240    #resize image width
size_h = 160    #resize image height 

#For Potential Resizing
#cam.set(3, size_w) #Overriding width of frame
#cam.set(4, size_h)  #Overriding height of fram

#Create Tab for the sliders
cv2.namedWindow('image')
#Create a Black image
img = np.zeros((300,512,3), np.uint8)

# create trackbars for color change
cv2.createTrackbar('H_min','image',0,255,nothing)
cv2.createTrackbar('S_min','image',0,255,nothing)
cv2.createTrackbar('V_min','image',0,255,nothing)

cv2.createTrackbar('H_max','image',0,255,nothing)
cv2.createTrackbar('S_max','image',0,255,nothing)
cv2.createTrackbar('V_max','image',0,255,nothing)
 
# def threshold_1(lowerb, upperb):
#     mask = cv2.inRange(img, lowerb, upperb)
#     output = cv2.bitwise_and(img,img,mask=mask)
#     return output

while(True):
    cv2.imshow('image',img)
    
    # get current positions of HSV_min and HSV_max trackbars
    H_min = cv2.getTrackbarPos('H_min','image')
    S_min = cv2.getTrackbarPos('S_min','image')
    V_min = cv2.getTrackbarPos('V_min','image')

    H_max = cv2.getTrackbarPos('H_max','image')
    S_max = cv2.getTrackbarPos('S_max','image')
    V_max = cv2.getTrackbarPos('V_max','image')
    #make this the array for mins and maxs
    lowerb = np.array([H_min, S_min, V_min], dtype="uint8")
    upperb = np.array([H_max, S_max, V_max], dtype="uint8")
    #print lower and upper threshold
    print("lowerb {} & upper{}",lowerb,upperb)

    #I have the frame to perform threshold 
    #I have the desired HSV threshold
    #record frame from camera
    ret, frame = cam.read()
    #make the frame from BGR to HSV
    frame_to_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #threshold
    thresh = cv2.inRange(frame_to_thresh,lowerb,upperb)
    cv2.imshow("thresh", thresh)



    #Exit pressing 'q'
    ch = cv2.waitKey(1) #run every 1 milisecond / if 10 then would wait 10 miliseconds
    if ch & 0xFF == ord('q'): #if not 64 bibt pc then if ch == ord('q)
        break

cv2.destroyAllWindows()