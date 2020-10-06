import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
	_, frame = cap.read()
	# BGR to HSV
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(image,100,200)
	cv2.imshow('cannyEdge', edges)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()