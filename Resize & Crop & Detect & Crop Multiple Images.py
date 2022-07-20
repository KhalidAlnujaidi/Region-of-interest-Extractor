import cv2
import glob
import os
import numpy as np

# Resize + Crop images in folder
# Find accurate ROI and crop accordingly

# Folder where images are located
inputFolder = r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\3"
# Create a folder to save images in (will not override if folder exists)
os.mkdir(r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\3\optimalImgs")

# counter to name images
i = 0

for img in glob.glob(inputFolder + "/*.jpg"):
    # load and resize
    image = cv2.imread(img)
    imgResize = cv2.resize(image, (900, 600))
    # initial crop based on manual measurements done
    roi = imgResize[150:450, 275:625]
    # Convert roi(cropped initial image) to RGB to proses
    imgGrey = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

    # creating mask and setting contrast boundaries
    lower = np.array([60, 60, 60])
    higher = np.array([110, 110, 110])
    # applying boundaries on img
    mask = cv2.inRange(imgGrey, lower, higher)

    # use mask to find contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #contourImage = cv2.drawContours(roi, contours, -1, 255, 3)
    see = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(see)

    # final and accurate ROI
    cropped_image = roi[y:y + h, x:x + w]

    # Write to matching directory made above || PLUG RESULT IMAGE
    cv2.imwrite(r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\3\optimalImgs\cropped_image%i.jpg" % i,
                cropped_image)  ## CHANGE RIO TO FINAL IMAGE
    i += 1
    cv2.imshow('image', cropped_image)
    cv2.waitKey(30)

cv2.destroyAllWindows()
