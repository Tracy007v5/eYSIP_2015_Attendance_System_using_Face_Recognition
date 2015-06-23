import numpy as np
import cv2

camera = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while(1):
	_, img = camera.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(
    	gray,
    	scaleFactor=1.3,
    	minNeighbors=5,
    	minSize=(30, 30),
    	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	for (x, y, w, h) in faces:
    		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow('img',img)
	if cv2.waitKey(1) == 27:
		break

	
camera.release()
cv2.destroyAllWindows()
