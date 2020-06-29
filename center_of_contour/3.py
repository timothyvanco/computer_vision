"""
In "Dice" folder you can find 15 photos of dice on a dark background.
Your goal is to locate the dices' centers.
For the time reasons, you don't have to make the algorithm fully robust,
if you are able to segment only some of the photos (even one), it's better
than having an almost super-duper algorithm, which is buggy.
"""

import os
import cv2
import numpy as np
import imutils
import argparse

#root_to_dice = 'dice'  # path to be changed if needed
#dice_images = [cv2.imread(os.path.join(root_to_dice, img_path)) for img_path in os.listdir(root_to_dice)]

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required=True, help="Path to the input picture")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

scale_percent = 40  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # resize image

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blurred, 70, 220)

# show image
cv2.imshow('canny', canny)
cv2.waitKey(0)

kernel_erosion = np.ones((1, 1), np.uint8)
erosion1 = cv2.erode(canny, kernel_erosion, iterations=1)

# show image after erosion1
cv2.imshow('erosion1', erosion1)
cv2.waitKey(0)

kernel_dilate = np.ones((2, 2), np.uint8)
dilate1 = cv2.dilate(erosion1, kernel_dilate, iterations=2)

# show image after dilate1
cv2.imshow('dilate1', dilate1)
cv2.waitKey(0)

kernel_erosion = np.ones((2, 2), np.uint8)
erosion2 = cv2.erode(dilate1, kernel_erosion, iterations=3)

# show image after erosion2
cv2.imshow('erosion2', erosion2)
cv2.waitKey(0)

# find contours in threshold image
cnts = cv2.findContours(erosion2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for contour in cnts:
    # compute center of contours
    M = cv2.moments(contour)
    cX = int(M["m10"] / (M["m00"] + 1e-7))
    cY = int(M["m01"] / (M["m00"] + 1e-7))

    # draw contour and center of the shape on image
    cv2.drawContours(resized, [contour], -1, (0, 255, 0), 2)
    cv2.circle(resized, (cX, cY), 7, (0, 0, 255), -1)
    cv2.putText(resized, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# show image
cv2.imshow('image', resized)
cv2.waitKey(0)

