import cv2
import glob
import os
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import numpy as np

# Resize + Crop images in folder
# Find accurate ROI and crop accordingly

# Folder where images are located
inputFolder = r"directory address of folder containing images"
# Create a folder to save images in (will not override if folder exists)
os.mkdir(r"directory address save images to")

# counter to name images
i = 0

for img in glob.glob(inputFolder + "/*.jpg"):
    # load and change color
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # AutoDetect object (Here is where the magic happens)
    bbox, label, conf = cv.detect_common_objects(gray)
    # get Y's and X's coordinates from box

    # temporary fix to when y1 is out of index
    try:
        y1 = bbox[0][1]
        y2 = bbox[0][3]
        x1 = bbox[0][0]
        x2 = bbox[0][2]
    except Exception as e:
        continue

    # Accurate ROI
    # Y:Y then X:X for obtained from boxx
    cropped_image = image[y1:y2, x1:x2]

    # Write to matching directory made above || PLUG RESULT IMAGE
    cv2.imwrite(r"directory address save images to \ outPutImageName%i.jpg" % i,
                cropped_image)  ## CHANGE RIO TO FINAL IMAGE
    i += 1
    cv2.imshow('image', cropped_image)
    cv2.waitKey(30)

cv2.destroyAllWindows()
