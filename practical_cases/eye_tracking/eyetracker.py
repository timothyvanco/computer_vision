import cv2

class EyeTracker:
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)


    def track(self, image):
        # functions track eyes in image - returns bounding box location - x, y, width, height of each face
        faceRects = self.faceCascade.detectMultiScale(image, scaleFactor=1.1,
                                                      minNeighbors=5, minSize=(30, 30),
                                                      flags=cv2.CASCADE_SCALE_IMAGE)
        rects = []
        for (fX, fY, fW, fH) in faceRects:
            # extract face Region of Interest (ROI) from image with numpy array slicing
            faceROI = image[fY:fY + fH, fX:fX + fW]
            rects.append((fX, fY, fX + fW, fY + fH))

            # EYE DETECTION
            eyeRects = self.eyeCascade.detectMultiScale(faceROI,
                                                        scaleFactor=1.1,
                                                        minNeighbors=10,
                                                        minSize=(20, 20),
                                                        flags=cv2.CASCADE_SCALE_IMAGE)

            for (eX, eY, eW, eH) in eyeRects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))


        return rects