"""
cv2.calcHist(images, channels, mask, histSize, ranges)

images      - image of which we want to compute histogram
channels    - list of indexes where we specify index of the channel we want to compute
            - grayscale [0], RGB [0, 1, 2]
mask        - if a mask is provided, histogram will be computed for masked pixels only
histSize    - number of bins we want to use, 32 = [32, 32, 32]
ranges      - specify range of possible pixel values (normally 0-256) for each channel

"""

import matplotlib.pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
