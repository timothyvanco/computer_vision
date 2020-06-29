import cv2

"""
PRE TRAINED CLASSIFIER
these classifiers work by scanning an image from left to right, and top to bottom, at varying scale sizes
Scanning an image from left to right and top to bottom is called the “sliding window” approach
As the window moves from left to right and top to bot- tom, one pixel at a time, 
the classifier is asked whether or not it “thinks” there is a face in the current window


detect function:

scaleFactor - How much the image size is reduced at each image scale. This value is used to create 
the scale pyramid in order to detect faces at multiple scales in the image (some faces may be closer to the foreground, 
and thus be larger; other faces may be smaller and in the background, thus the usage of varying scales). 
A value of 1.05 indicates that it will be reducing the size of the image by 5% at each level in the pyramid.

minNeighbors - How many neighbors each window should have for the area in the window to be considered a face. 
The cascade classifier will detect multiple windows around a face. This parameter controls how many 
rectangles (neighbors) need to be detected for the window to be labeled a face.

minSize - A tuple of width and height (in pixels) indicating the minimum size of the window. 
Bounding boxes smaller than this size are ignored. It is a good idea to start with (30, 30) and fine-tune from there.

RETURN - rects
list of tuples containing the bounding boxes of the faces in the image. 
These bounding boxes are simply the (x, y) location of the face, along with the width and height of the box.

"""

class FaceDetector:
    def __init__(self, faceCascadePath):
        # pre-tarined classifier to recognize faces
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath) # path to classifier - XML file

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
        rects = self.faceCascade.detectMultiScale(image,
                                                  scaleFactor = scaleFactor,
                                                  minNeighbors = minNeighbors,
                                                  minSize = minSize,
                                                  flags= cv2.CASCADE_SCALE_IMAGE)


        return rects

