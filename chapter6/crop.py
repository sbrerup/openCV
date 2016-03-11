# crop.py

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#40 = y start, 450 = y slut. Gælder også for x
cropped = image[40:450, 440:730]
cv2.imshow("Baby Face", cropped)
cv2.waitKey(0)
