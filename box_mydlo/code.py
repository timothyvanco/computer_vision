import cv2
import numpy as np
import imutils

image = cv2.imread('pictures/prepravka1.png', cv2.IMREAD_UNCHANGED)
cv2.imshow("image", image)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("image", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
