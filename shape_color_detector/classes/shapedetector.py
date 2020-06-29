import cv2

class ShapeDetector:
    def __init__(self):
        pass                # skip init part

    def detect(self, contour):
        shape = "unidentified"
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True) # Douglas–Peucker algorithm
        # Contour approximation is predicated on the assumption that a curve
        # can be approximated by a series of short line segments

        # triangle -> 3 vertices
        if len(approx) == 3:
            shape = "triangle"

        # 4 vertices -> square/rectangle
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # square will have aspect ratio that is approx. equal to one
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

        elif len(approx) == 5:
            shape = "pentagon"

        else:
            shape = "circle"

        return shape
