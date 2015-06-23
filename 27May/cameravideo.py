import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(1):
 ret, Frame = cap.read()
 gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
 cv2.imshow('Frame',Frame)
 if cv2.waitKey(1)=='s':
 	cv2.imwrite('Frame.jpeg',gray)
  	break

cap.release()
cv2.destroyAllWindows()
