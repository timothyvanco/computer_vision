"""
goal: How do I compute the center of a contour using Python and OpenCV?

1) detect the outline of each shape in the image
2) compute the center of the contour — also called the centroid of the region

image preprocessing:
1) Conversion to grayscale
2) Blurring to reduce high frequency noise to make contour detection more accurate
3) Binarization of the image (thresholding)
"""

import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load image, convert to grayscale, blur it slightly, threshold it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in threshold image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for contour in cnts:
    # compute center of contours
    M = cv2.moments(contour)
    cX = int(M["m10"] / (M["m00"] + 1e-7))
    cY = int(M["m01"] / (M["m00"] + 1e-7))

    # draw contour and center of the shape on image
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show image
    cv2.imshow('image', image)
    cv2.waitKey(0)
