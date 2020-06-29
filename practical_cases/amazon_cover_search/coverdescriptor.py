import numpy as np
import cv2

class CoverDescriptor:
    def __init__(self, useSIFT=False):
        self.useSIFT = useSIFT

    # extract both keypoints and descriptors from an image
    def describe(self, image):
        descriptor = cv2.BRISK_create()

        if self.useSIFT:
            descriptor = cv2.xfeatures2d.SIFT_create()

        # keypoint detection is the “detect” phase,
        # whereas the actual description of the region is the “compute” phase
        (kps, descs) = descriptor.detectAndCompute(image, None)
        kps = np.float32([kp.pt for kp in kps])

        return (kps, descs)

