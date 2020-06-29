import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)


"""
AVERAGING
Define a k × k sliding window on top of our image, where k is always an odd number. 
This window is going to slide from left-to-right and from top-to-bottom. 
The pixel at the center of this ma- trix (we have to use an odd number, 
otherwise there would not be a true “center”) is then set to be the average of all other pixels surrounding it.
"""

# imagine we want to blur and size of kernel
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])
cv2.imshow("Averaged", blurred)
cv2.imwrite("Averaged_blurred.jpg", blurred)
cv2.waitKey(0)


"""
GAUSSIAN
Gaussian blurring is similar to average blurring, but instead of using a simple mean, 
we are now using a weighted mean, where neighborhood pixels that are closer to the central 
pixel contribute more “weight” to the average.
"""
blurred = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5 ,5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])
cv2.imshow("Gaussian", blurred)
cv2.imwrite("Gaussian_blurred.jpg", blurred)
cv2.waitKey(0)


"""
MEDIAN
By definition, the median pixel must exist in our neighborhood. 
By replacing our central pixel with a median rather than an average, we can substantially reduce noise.
"""
blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])
cv2.imshow("Median", blurred)
cv2.imwrite("Median_blurred.jpg", blurred)
cv2.waitKey(0)


"""
BILATERAL
In order to reduce noise while still maintaining edges, 
we can use bilateral blurring. Bilateral blurring accomplishes this 
by introducing two Gaussian distributions.
this method is able to preserve edges of an image, while still reducing noise. 
The largest downside to this method is that it is considerably slower than its averaging, 
Gaussian, and median blurring counterparts.
"""
# image, diameter of pixel neighborhood, color o (larger value - more colors in neighborhood), space o
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral", blurred)
cv2.imwrite("Bilateral_blurred.jpg", blurred)
cv2.waitKey(0)