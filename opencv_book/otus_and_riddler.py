import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# OTSU
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh1 = cv2.bitwise_not(thresh)

# RIDDLER
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh2 = cv2.bitwise_not(thresh)

stack = np.hstack((blurred, thresh1, thresh2))
cv2.imshow("otsu_riddler", stack)
cv2.imwrite("otsu_riddler.jpg", stack)
cv2.waitKey(0)
