import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.waitKey(0)
cv2.imshow("Green", G)
cv2.waitKey(0)
cv2.imshow("Blue", B)
cv2.waitKey(0)

stack = np.hstack((R, G, B))
cv2.imshow("stack", stack)
cv2.imwrite("splitting.jpg", stack)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.imwrite("merging.jpg", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype="uint8")
red_merge = cv2.merge([zeros, zeros, R])
green_merge = cv2.merge([zeros, G, zeros])
blue_merge = cv2.merge([B, zeros, zeros])

canvas = np.hstack((red_merge, green_merge, blue_merge))
cv2.imshow("canvas", canvas)
cv2.imwrite("merged.jpg", canvas)
cv2.waitKey(0)











