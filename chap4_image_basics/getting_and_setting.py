# getting and setting.py

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

b,g,r = image[0,0]

print("Pixel at (0,0) - red: {}, green: {}, blue: {}".format(r,g,b))

image[0,0] = (0,0,255)
b,g,r = image[0,0]

print("Pixel at (0,0) - Red: {}, green: {}, blue {}".format(r,g,b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0,255,0)

cv2.imshow("updated", image)

cv2.waitKey(0)
