import numpy as np
import argparse
import random
import time
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-m", "--mask-rcnn", required=True, help="Base path to the mask-rcnn directory")
ap.add_argument("-v", "--visualize", type=int, default=0, help="If visualize each instance")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="Minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3, help="Minimum threshold for pixel-wise mask segmentation")
args = vars(ap.parse_args())

# load COCO class labels Mask R-CNN was trained on
labelsPath = os.path.sep.join([args["mask_rcnn"], "object_detection_classes_coco.txt"])
LABELS = open(labelsPath).read().strip().split("\n")

# load set of colors what will be used when visualizing an instance segmentation
colorsPath = os.path.sep.join([args["mask_rcnn"], "colors.txt"])
COLORS = open(colorsPath).read().strip().split("\n")
COLORS = [np.array(c.split(",")).astype("int") for c in COLORS]
COLORS = np.array(COLORS, dtype="uint8")

weightsPath = os.path.sep.join([args["mask_rcnn"], "frozen_inference_graph.pb"])
configPath = os.path.sep.join([args["mask_rcnn"], "mask_rcnn_inception_v2_coco_2018_01_28.pbtxt"])

# load Mask R-CNN trained on the COCO dataset (90 classes) from disk
print("[INFO] loading Mask R-CNN from disk...")
net = cv2.dnn.readNetFromTensorflow(weightsPath, configPath)

image = cv2.imread(args["image"])
(H, W) = image.shape[:2]

# construct a blob from input image and then perform forward pass of the Mask R-CNN
# giving us bounding box coordinates of the objects in the image along with the pixel-wise
# segmentation for each specific object
blob = cv2.dnn.blobFromImage(image, swapRB=True, crop=False)
net.setInput(blob)

start = time.time()
(boxes, masks) = net.forward(["detection_out_final", "detection_masks"])
end = time.time()

# show time information and volume info on Mask R-CNN
print("[INFO] Mask R-CNN took {:.6f} seconds".format(end - start))
print("[INFO] boxes shape: {}".format(boxes.shape))
print("[INFO] masks shape: {}".format(masks.shape))

clone = image.copy() # clone it so I can draw on it

# loop over detected objects
for i in range(0, boxes.shape[2]):
    # extract class ID of the detection along with confidence (probability) associated with prediction
    classID = int(boxes[0, 0, i, 1])
    confidence = boxes[0, 0, i, 2]

    # filter weak predictions
    if confidence > args["confidence"]:


        box = boxes[0, 0, i, 3:7] * np.array([W, H, W, H])
        (startX, startY, endX, endY) = box.astype("int")
        boxW = endX - startX
        boxH = endY - startY

        # extract pixel-wise segmentation for the object, resize mask such that
        # it's same dimensions of the bounding box and finally threshold to create binary mask
        mask = masks[i, classID]
        mask = cv2.resize(mask, (boxW, boxH), interpolation=cv2.INTER_NEAREST)
        mask = (mask > args["threshold"])

        roi = clone[startY:endY, startX:endX] # extract ROI of image

        if args["visualize"] > 0:
            # convert mask from a boolean to an integer mask with values: 0-255
            visMask = (mask * 255).astype("uint8")
            instance = cv2.bitwise_and(roi, roi, mask=visMask)

            # show extracted ROI, mask, with segmented instance
            cv2.imshow("ROI", roi)
            cv2.imshow("Mask", visMask)
            cv2.imshow("Segmented", instance)


        # extract only masked region of the ROI by passing in the boolean mask
        # array as slice condition
        roi = roi[mask]

        # randomly select color for visualisation
        color = random.choice(COLORS)
        blended = ((0.4 * color) + (0.6 * roi)).astype("uint8")

        clone[startY:endY, startX:endX][mask] = blended

        # draw bounding box of the instance on image
        color = [int(c) for c in color]
        cv2.rectangle(clone, (startX, startY), (endX, endY), color, 2)

        # draw predicted label
        text = "{}: {:.4f}".format(LABELS[classID], confidence)
        cv2.putText(clone, text, (startX, startY - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv2.imshow("Output", clone)
cv2.imwrite("Mask_R-CNN.jpg", clone)
cv2.waitKey(0)