import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (0, 100, 255)
#more info = https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
#We are going to get more information from contours
objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')
for c in contours:
    #[c] list of a single contour , -1 all contorus, color, -1 completely fill
    cv2.drawContours(objects,[c],-1,color,-1) 

    #get some information about our contours = 
    # Area = asnwer is in pixel^2
    area = cv2.contourArea(c)
    # perimeter = true means the ark is a closed loop 
    perimeter = cv2.arcLength(c,True)
    #Calculate the Centroid
    #first calculate the moment
    M = cv2.moments(c)
    #Calculate centroid centers
    cx = int(M['m10']/M['m00']) #int () to cast the value we are about to create 
    cy = int(M['m01']/M['m00'])
    #Draw centroid
    cv2.circle(objects,(cx,cy),4,(0,0,100),-1) # 4 for the radious of the pixels / radius of centroid indicator
    print("Area: {}, perimeter: {}".format(area,perimeter))

cv2.imshow("contour",objects )
cv2.waitKey(0)
cv2.destroyAllWindows()
