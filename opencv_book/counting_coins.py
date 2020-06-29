import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])

# we have to resize image but retain aspect ratio
d = 1024 / image.shape[1]
dimension = (1024, int(image.shape[0] * d))
image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
<<<<<<< HEAD
blurred = cv2.GaussianBlur(gray, (13, 13), 0)

edged = cv2.Canny(blurred, 30, 150)
=======
blurred = cv2.GaussianBlur(gray, (19, 19), 0)

edged = cv2.Canny(blurred, 40, 150)
>>>>>>> f8b2573345e2d3cee7c0dddeccc29a5baccc7906
cv2.imwrite("edged.jpg", edged)

# 1 argument - function is destructive to the image you pass in -> copy of image
# 2 argument - type of contours I want, I want contours that follow the outline of the coin
# 3 argument - how I want to approximate the contour
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))

# not to draw on original image - make copy
coins = image.copy()

# input image, list of contours, -1 = indicating to draw all of contours, color, thickness
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imwrite("coins.jpg", coins)


image_stack1 = cv2.imread("edged.jpg")
image_stack2 = cv2.imread("coins.jpg")

stack = np.hstack((image, image_stack1, image_stack2))

cv2.imwrite("counting_coins.jpg", stack)
cv2.imshow("counting_coins", stack)
cv2.waitKey(0)

hstack1 = []
hstack2 = []

# method finds the “enclosing box” that our contour will fit into, allowing us to crop it from the image.
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    # crop coin from image
    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    hstack1.append(coin)
    cv2.imshow("Coin", coin)
    cv2.waitKey(0)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    # fits a circle to a contour
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]

    # show only the foreground of the coin and ignore the background - background removed
    masked_coin = cv2.bitwise_and(coin, coin, mask = mask)
    hstack2.append(masked_coin)
    cv2.imshow("Masked Coin", masked_coin)
    cv2.waitKey(0)
