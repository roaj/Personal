import numpy as np
import cv2

#importing image
img = cv2.imread("faces.jpeg",1)
#pass it to grayScale
gray = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)
