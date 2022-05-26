from sre_constants import SUCCESS
import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    _, img = cap.read()

    cv2.imshow("Result", img)
    if cv2.waitKey(1) == ord('q'):
    break