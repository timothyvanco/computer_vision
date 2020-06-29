import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",  required=True, help="Path to the input picture")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
scale_percent = 40  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # resize image
img = resized

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# show image thresh
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

canny = cv2.Canny(thresh, 70, 220)

# show image thresh
cv2.imshow('canny', canny)
cv2.waitKey(0)

# sure background area
sure_bg = cv2.dilate(canny, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(canny,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

# show image img
cv2.imshow('img', img)
cv2.waitKey(0)