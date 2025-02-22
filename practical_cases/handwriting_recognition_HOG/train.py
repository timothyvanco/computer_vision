from sklearn.externals import joblib
from sklearn.svm import LinearSVC       # use SVM to train
from hog import HOG
import dataset

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to the dataset file")
ap.add_argument("-m", "--model", required=True, help="path to where model will be stored")
args = vars(ap.parse_args())

(digits, target) = dataset.load_digits(args["dataset"])
data = []

hog = HOG(orientations = 18, pixelsPerCell = (10, 10), cellsPerBlock = (1, 1), transform = True)

for image in digits:
    image = dataset.deskew(image, 20)
    image = dataset.center_extent(image, (20, 20))
    hist = hog.describe(image)
    data.append(hist)

model = LinearSVC(random_state=42)
model.fit(data, target)

joblib.dump(model, args["model"])   # save model for future usage
