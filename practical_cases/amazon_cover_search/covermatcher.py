import numpy as np
import cv2

class CoverMatcher:
    # ratio - ratio of nearest neighbor distances suggested by Lowe to prune down
    #          the number of key- points a homography needs to be computed for
    # minMatches - The minimum number of matches required for a homography to be calculated
    # useHamming - boolean indicating whether the Hamming or Euclidean distance should be used to compare feature vectors
    def __init__(self, descriptor, coverPaths, ratio=0.7, minMatches=40, useHamming=True):
        self.descriptor = descriptor
        self.coverPaths = coverPaths
        self.ratio = ratio
        self.minMatches = minMatches
        self.distanceMethod = "BruteForce"

        if useHamming:
            self.distanceMethod += "-Hamming"


    # The goal of this method is to take the keypoints and descriptors from the query image
    # and then match them against a database of keypoints and descriptors.
    # entry in the database with the best “match” will be chosen as the identification of the book cover.
    def search(self, queryKps, queryDescs):
        # key of the dictionary will be the unique book cover filename
        # value will be the matching percentage of keypoints
        results = {}

        for coverPath in self.coverPaths:
            cover = cv2.imread(coverPath)
            gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
            (kps, descs) = self.descriptor.describe(gray)

            # number of matched keypoints is then determined using the match method
            score = self.match(queryKps, queryDescs, kps, descs)
            results[coverPath] = score

        if len(results) > 0:
            results = sorted([(v, k) for (k, v) in results.items() if v > 0], reverse=True)

        return results

    # kpsA - list of keypoints associated with the first image to be matched
    # featuresA - list of feature vectors associated with the first image to be matched
    # kpsB - list of keypoints associated with the second image to be matched
    # featuresB - list of feature vectors associated with the second image to be matched
    def match(self, kpsA, featuresA, kpsB, featuresB):
        matcher = cv2.DescriptorMatcher_create(self.distanceMethod)
        # knn - k-nearest-neighbor = smallest Euclidean dis- tance between feature vectors
        rawMatches = matcher.knnMatch(featuresB, featuresA, 2) # find 2 nearest neighbors for each feature vector
        matches = []

        for m in rawMatches:
            # This test helps remove false matches and prunes down the number of keypoints
            # the homography needs to be com- puted for, thus speeding up the entire process
            if len(m) == 2 and m[0].distance < m[1].distance * self.ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        if len(matches) > self.minMatches:
            ptsA = np.float32([kpsA[i] for (i, _) in matches])
            ptsB = np.float32([kpsB[j] for (_, j) in matches])
            (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)

            return float(status.sum()) / status.size

        return -1.0


