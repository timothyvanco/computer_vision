"""
Thresholding is the binarization of an image.
In general, we seek to convert a grayscale image to a binary image,
where the pixels are either 0 or 255.

A simple thresholding example would be selecting a pixel value p,
and then setting all pixel intensities less than p to zero,
and all pixel values greater than p to 255.
"""

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)
cv2.waitKey(0)

# threshold value is 155, then maximum value in thresholding - any pixel bigger than 155 -> 255, else zero
(T, thresh) = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

(T, threshInv) = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary", threshInv)
cv2.waitKey(0)

bitwise = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Coins", bitwise)
cv2.waitKey(0)

stack = np.hstack((image, thresh, threshInv, bitwise))
cv2.imshow("stack", stack)
cv2.imwrite("thresholding.jpg", stack)
cv2.waitKey(0)