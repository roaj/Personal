import numpy as np
import cv2

# segmentation = process to get an object from an image, product is a binary image
# result of only what you need
   
    # thresholding algorithm = type of segmentation that does a look at values of the source image and compares it to a ones's central value 
    # to decide whether a single pixel or group of pixel should have a value of zero or one

bw = cv2.imread('detect_blob.png',0) # import as a b&w image
height, width = bw.shape[0:2]

cv2.imshow("original",bw)

#initialize Binary variable

binary = np.zeros([height,width,1],'uint8')

#set threshold / every pixel will be compared to this value

thresh = 85

for row in range(0,height):
    for col in range(0,width):
        if bw[row][col] > thresh:
            binary[row][col]=255  # or 0 

cv2.imshow("slow binary", binary)

#OTher MEthod

ret, thresh = cv2.threshold(bw,thresh,255, cv2.THRESH_BINARY)
cv2.imshow("CV threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()


