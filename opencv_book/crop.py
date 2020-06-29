import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# startY : endY, startX:endX
cropped = image[30:120, 240:335]
cv2.imshow("T-rex Face", cropped)
cv2.waitKey(0)

