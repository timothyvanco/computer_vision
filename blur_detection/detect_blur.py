from imutils import paths
import argparse
import cv2
import time

def variance_of_laplacian(image):
    # compute Laplacian of the image and then return focus measure,
    # which is simply the variance of Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=False, help="path to input directory of images")
ap.add_argument("-v", "--video", required=False, help="path to the input video")
ap.add_argument("-t", "--threshold", type=float, default=100.0, help="focus measure that fall below this value"
                                                                     "will be considered 'blurry'")
args = vars(ap.parse_args())

camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not blurry"

    if fm < args["threshold"]:
        text = "Blurry"

    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
