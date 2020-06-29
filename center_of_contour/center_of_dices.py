import imutils
import numpy as np
import cv2
import os

root_to_dice = 'dice'  # path to be changed if needed
dice_images = [cv2.imread(os.path.join(root_to_dice, img_path)) for img_path in os.listdir(root_to_dice)]

for image in dice_images:
    scale_percent = 40  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # resize image

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 70, 220)

    kernel_dilate = np.ones((10, 10), np.uint8)
    dilate = cv2.dilate(canny, kernel_dilate, iterations=3)

    kernel_erosion = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(dilate, kernel_erosion, iterations=6)

    # find contours in threshold image
    cnts = cv2.findContours(erosion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for contour in cnts:
        # compute center of contours
        M = cv2.moments(contour)
        cX = int(M["m10"] / (M["m00"] + 1e-7))
        cY = int(M["m01"] / (M["m00"] + 1e-7))

        # draw contour and center of the shape on image
        cv2.drawContours(resized, [contour], -1, (0, 255, 0), 2)
        cv2.circle(resized, (cX, cY), 7, (0, 0, 255), -1)
        cv2.putText(resized, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # show image
    cv2.imshow('image', resized)
    cv2.waitKey(0)

