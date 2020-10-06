'''
This file tracks red objects USING BGR INSTEAD OF HSV
The following code is adapted from the OpenCV tutorials (changing color space)
and contours in particular. Drawing the bounding boxes was taken from
stackoverflow, the tutorial was confusing me. Makes sense what s/he did.
Modified it to work when no red contours are present (would crash due to
attempting to due np.argmax of empty array)

BGR is worse due to the ranges being difficult to work with,
The range I inputted needs the object to be perfectly red with
no lighting issues.
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame from camera
    _, frame = cap.read()

    # define range of blue color in HSV
    lower_red = np.array([0,0,75])
    upper_red = np.array([30,30,255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(frame, lower_red, upper_red)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    if areas:
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt=contours[max_index]

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
# -------------------------------------------------------------------

    cv2.imshow('frame',frame)
    #cv2.imshow('im4',im4)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()