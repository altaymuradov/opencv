from platform import release
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red
    low_red = np.array([0, 100, 20])
    high_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Blue
    low_blue = np.array([78, 158, 124])
    high_blue = np.array([138, 255, 255])
    blue_mask = cv2.inRange(hsv, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Yellow
    low_yellow = np.array([22, 93, 0])
    high_yellow = np.array([45, 255, 255])
    yellow_mask = cv2.inRange(hsv, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    cv2.imshow('frame', frame)
    #cv2.imshow('Red Mask', red)
    cv2.imshow('Blue mask', blue)
    #cv2.imshow('yellow', yellow)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
