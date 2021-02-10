import numpy as np
import cv2

#importing image
img = cv2.imread("faces.jpeg",1)    #pass it to grayScale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
path = "haarcascade_frontalface_default.xml"


#create castace object  = loads the xml files and initializes our cascade of function and classifier 
#this object is what we use to create the face detection algorithm 
    #contains many functions and many classifier and a function to pass in an image to detect faces 
face_cascade = cv2.CascadeClassifier(path)

#lets run that function
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.10, minNeighbors = 8, minSize=(40,40))
#this returns a list that contains all the bounding bboxes for detected faces such as boundary
print(len(faces))

#draw boxes
    
for (x,y,w,h) in faces: #indicating that each element in face object /
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
