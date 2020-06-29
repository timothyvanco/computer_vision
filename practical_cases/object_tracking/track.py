import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

whiteLower = np.array([200, 200, 200], dtype="uint8")
whiteUpper = np.array([255, 255, 255], dtype="uint8")

camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()

    # if it was succesfully grabbed from video
    if not grabbed:
        break       # if it is the end of video

    # frame - frame itself
    white = cv2.inRange(frame, whiteLower, whiteUpper)
    white = cv2.GaussianBlur(white, (3, 3), 0)

    (cnts, _) = cv2.findContours(white.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", white)

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
