import cv2
import numpy as np

# Getting image ready #

#load raw img
rawImage = cv2.imread("cropped.jpg")
#resize image if needed and create copy for applying end result
img = cv2.resize(rawImage, (900, 600))
img_copy = img.copy()
# Convert to RGB
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img setup complete



# setting contrast boundries
lower = np.array([60, 60, 60])
higher = np.array([110, 110, 110])
# applying boundaries on img
mask = cv2.inRange(imgGrey, lower, higher)
print(mask.shape)
# show masked img
cv2.imshow("mask", mask)


# use mask to find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contourImage = cv2.drawContours(img, contours, -1, 255, 3)
see = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(see)
# draw rec based on found contours
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# show contourImage
cv2.imshow("contourImage", contourImage)

# GET CROPPED IMAGE
cropped_image = img_copy[y:y+h,x:x+w]
cv2.imshow("end", cropped_image)


cv2.waitKey(0)
