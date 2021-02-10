import numpy as np
import cv2



img = cv2.imread('sudoku.png',0)
cv2.imshow("original", img)

#show basic treshold techinic

ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("basic binary ", thresh_basic)

#adaptive Thresholding

thresh_adapt = cv2. adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 201, 1)
cv2.imshow("adaptive_thesholding", thresh_adapt)


cv2.waitKey(0)
cv2.destroyAllWindows()