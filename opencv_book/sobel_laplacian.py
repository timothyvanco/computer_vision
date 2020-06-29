import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image which wants to be computed gradient magnitude, second argument - data type for output image
# In order to ensure you catch all edges, use a floating point data type,
# then take the absolute value of the gradient im- age and convert it back to an 8-bit unsigned integer
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

stack = np.hstack((image, sobelX, sobelY, sobelCombined))
cv2.imshow("stack", stack)
cv2.imwrite("sobel_laplacian.jpg", stack)
cv2.waitKey(0)



