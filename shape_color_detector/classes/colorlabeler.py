from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class ColorLabeler:
    def __init__(self):
        colors = OrderedDict({
            "red": (0, 0, 255),
            "green": (0, 255, 0),
            "blue": (255, 0, 0),
            "yellow": (0, 255, 255),
            "orange": (0, 70, 255)
        })

        # allocate memory for L*a*b*,. then initialize color names list
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []

        for (i, (name, rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)

        # convert L*a*b* array from RGB color space to L*a*b*
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_BGR2LAB)

    def label(self, image, c):
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]

        minDist = (np.inf, None)  # minimum distance

        for (i, row) in enumerate(self.lab):
            # compute distance between current L*a*b* color value and mean
            d = dist.euclidean(row[0], mean)
            if d < minDist[0]:
                minDist = (d, i)

        return self.colorNames[minDist[1]]
