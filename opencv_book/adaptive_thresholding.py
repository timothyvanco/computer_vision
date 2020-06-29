import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# image which want to be thresholded, maximum value 255, ..., neighborhood size 11x11 pixels, parameter C = 4 - integer that is subtracted from mean -> fine tuning
thresh1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 5)

thresh2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 5)

stack = np.hstack((image, thresh1, thresh2))
cv2.imshow("adaptive thresholding", stack)
cv2.imwrite("adaptive_thresholding.jpg", stack)
cv2.waitKey(0)
