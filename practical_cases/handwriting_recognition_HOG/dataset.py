from pyimagesearch import imutils
import numpy as np
import mahotas
import cv2

def load_digits(datasetPath):
    data = np.genfromtxt(datasetPath, delimiter = ",", dtype="uint8") # 8 bit integer - pixel values always 0-255
    target = data[:, 0]     # target 0-9 of number
    data = data[:, 1:].reshape(data.shape[0], 28, 28) # all columns after first one - pixel intensities of image

    return (data, target)


# 1 argument - image of the digit that is going to be deskewed
# 2 argument - width that the image is going to be resized to
def deskew(image, width):
    (h, w) = image.shape[:2]
    moments = cv2.moments(image) # moments contain statistical information regarding distribution of the location of white pixels in image

    skew = moments["mu11"] / moments["mu02"]
    M = np.float32([
        [1, skew, -0.5 * w * skew],
        [0, 1, 0]
    ])
    # flags parameter controls how the image is going to be deskewed
    image = cv2.warpAffine(image, M, (w, h), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    image = imutils.resize(image, width=width)

    return image

# 1 arg - deskewed image
# 2 arg - output size of image
def center_extent(image, size):
    (eW, eH) = size

    # if width is bigger than height
    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width = eW)
    else:
        image = imutils.resize(image, height= eH)

    extent = np.zeros((eH, eW), dtype="uint8")

    offsetX = (eW - image.shape[1]) // 2
    offsetY = (eH - image.shape[0]) // 2

    extent[offsetY:offsetY + image.shape[0], offsetX:offsetX + image.shape[1]] = image

    CM = mahotas.center_of_mass(extent) # returns the weighted (x, y) coordinates of the center of the image
    (cY, cX) = np.round(CM).astype("int32") # convert into integers than floats

    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    M = np.float32([[1, 0, dX], [0, 1, dY]])
    extent = cv2.warpAffine(extent, M, size)

    return extent # return centered image