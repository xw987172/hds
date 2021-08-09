#coding: utf-8
import cv2
import numpy as np
print("cv2 version :",cv2.__version__)

cap = cv2.VideoCapture(0)
cap.set(3,360)
cap.set(4,480)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)

    k =cv2.waitKey(30) &0xff
    if k ==27: # 'ESC'
        break
