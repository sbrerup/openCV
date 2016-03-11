# resize.py

import numpy as np
import argparse
import imutils as iu
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

#interpolation can also be
#.INTER_LINEAR, .INTER_CUBIC, .INTER_NEAREST
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resize (Width)", resized)

#resize by height
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (height)", resized)
cv2.waitKey(0)

resized = iu.resize(image, width = 500)
cv2.imshow("Resized with imutils function", resized)
cv2.waitKey(0)
