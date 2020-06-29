import numpy as np
import argparse
import cv2
import os

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True, help="Path to input image file")
#args = vars(ap.parse_args())
#image = cv2.imread(args["image"])

root_to_dice = 'images'  # path to be changed if needed
dice_images = [cv2.imread(os.path.join(root_to_dice, img_path)) for img_path in os.listdir(root_to_dice)]

for image in dice_images:
    scale_percent = 60  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)  # background - black, text - white

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # take (x, y) coordinates of all pixel values > 0, use them to compute
    # rotated bounding box that contains all coordinates
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]  # returns angle values in the range [-90, 0)

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    print("[INFO] angle: {:.3f}".format(angle))
    stack = np.hstack((image, rotated))
    cv2.imshow("Stack", stack)
    cv2.imwrite("image1.png", stack)
    cv2.waitKey(0)
    break



