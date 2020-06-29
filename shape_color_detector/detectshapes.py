from classes.shapedetector import ShapeDetector
from classes.colorlabeler import ColorLabeler
import imutils
import cv2

image = cv2.imread('image.png', cv2.IMREAD_UNCHANGED)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

sd = ShapeDetector()
cl = ColorLabeler()

for c in cnts:
    # compute center of contour
    M = cv2.moments(c)
    cX = int(M["m10"] / (M["m00"] + 1e-7))
    cY = int(M["m01"] / (M["m00"] + 1e-7))

    # find shape of contour/object
    shape = sd.detect(c)
    color = cl.label(lab, c)

    c = c.astype("float")
    c = c.astype("int")
    text = "{} {}".format(color, shape)

    # draw contour and put text
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("image", image)
    cv2.waitKey(0)


