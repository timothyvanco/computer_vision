import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flipped_H = cv2.flip(image, 1)
cv2.imshow("Flipped Horizintally", flipped_H)
cv2.waitKey(0)

flipped_V = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped_V)
cv2.waitKey(0)

flipped_HV = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped_HV)
cv2.waitKey(0)

stack1 = np.hstack((image, flipped_H))
stack2 = np.hstack((flipped_V, flipped_HV))
stack = np.vstack((stack1, stack2))
cv2.imshow("Flipped images", stack)
cv2.imwrite("Stack_flipped.jpg", stack)
cv2.waitKey(0)

