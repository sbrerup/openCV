#translation.py

import numpy as np
import argparse
import imutils as iu
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)

M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)

shifted = iu.translate(image, 0, 100)
cv2.imshow("Shifted down", shifted)
cv2.waitKey(0)
