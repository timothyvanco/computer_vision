# MASK R-CNN

The Mask R-CNN is a Convolution Neural Network algorithm, which was introduced by He et al. in their 2017 paper, Mask R-CNN.
Mask R-CNN builds on the previous object detection work of R-CNN (2013), Fast R-CNN (2015), and Faster R-CNN (2015), all by Girshick et al.

The original R-CNN algorithm is a four-step process:

Step #1: Input an image to the network.
Step #2: Extract region proposals (i.e., regions of an image that potentially contain objects) using an algorithm such as Selective Search.
Step #3: Use transfer learning, specifically feature extraction, to compute features for each proposal (which is effectively an ROI) using the pre-trained CNN.
Step #4: Classify each proposal using the extracted features with a Support Vector Machine (SVM).

![image_mask_r_cnn](mask-r-cnn-howto.png)

However, the problem with the R-CNN method is it’s incredibly slow. To improve upon the original R-CNN, Girshick et al. published the Fast R-CNN algorithm:

My result is here:

![myresult-mask-r-cnn](Mask_R-CNN.jpeg)
