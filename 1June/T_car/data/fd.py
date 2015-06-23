import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('cascade.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('test-143.pgm')
height, width, channels = img.shape
img1 = cv2.resize(img,(width*2, height*2), interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img1, 1.22, 5)
for (x,y,w,h) in faces:
 cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
 roi_gray = gray[y:y+h, x:x+w]
 roi_color = img1[y:y+h, x:x+w]
#eyes = eye_cascade.detectMultiScale(roi_gray)	
#for (ex,ey,ew,eh) in eyes:
#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img1)
cv2.imwrite('car detected-01.png',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
