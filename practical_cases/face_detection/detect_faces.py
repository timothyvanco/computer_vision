from facedetector import FaceDetector
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
ap.add_argument("-i", "--image", required=True, help="path to where the image file resides")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


fd = FaceDetector(args["face"])
# if there is wrong face detection - change scaleFactor then minNeighbors
faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
print("I found {} face(s)".format(len(faceRects)))

# each bounding box is just a tuple with four values:
# the x and y starting location of the face in the image,
# followed by the width and height of the face.
for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.imwrite("me.jpg", image)
cv2.waitKey(0)
