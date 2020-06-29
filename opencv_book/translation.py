import numpy as np
import argparse
import imutils  # for common tasks like translation, rotation, resizing
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# translation matrix, how many pixels down and right will be shifted
# [1, 0, tx] - tx = how many pixels shift to right, negative -> left
# [0, 1, ty] - ty = how many pixels shift to down, negative -> up
M = np.float32([[1, 0, 25], [0, 1, 50]])            # floating point array, shifting down right

# image, translation matrix, dimensions (width, height)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])          # shifting up left
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

