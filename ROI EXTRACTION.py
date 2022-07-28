import glob
import os
import cv2
import numpy as np
import cvlib as cv


# Folder where images are located
inputFolder = r"C:\Users\Majid Alnujaidi\Desktop\ImageData\4"
# Create a folder to save images in (will not override if folder exists)
os.mkdir(r"C:\Users\Majid Alnujaidi\Desktop\ROI\4")

# counter to name images
i = 1

# Travers all images in directory
for img in glob.glob(inputFolder + "/*.jpg"):
    # read image
    raw_img = cv2.imread(img)

    # Resize and Preserve Aspect Ratio
    scale_percent = 30
    width = int(raw_img.shape[1] * scale_percent / 100)
    height = int(raw_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv2.resize(raw_img, dim, interpolation=cv2.INTER_AREA)

    # To Gray
    raw_img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Erosion and Dilation
    kernel = np.ones((5, 5), np.uint8)
    erodeGrayImg = cv2.erode(raw_img_gray, kernel, iterations=3)
    dilateImg = cv2.dilate(erodeGrayImg, kernel, iterations=3)

    # Blurr image
    blurrImg = cv2.GaussianBlur(dilateImg, (3, 3), cv2.BORDER_DEFAULT)

    # Apply Canny
    imgCanny = cv2.Canny(blurrImg, 0, 100, L2gradient=True)

    # Threshold and find Contours
    ret, thresh = cv2.threshold(imgCanny, 0, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Extract coordinates for contour with the largest area
    coordinates = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(coordinates)

    # Cropping of raw (resized) img
    resized_img = resized_img[(y - 50):(y + h) + 50, (x - 50):(x + w) + 50]
    # The +- 20 for some space around ROI

    # Save the image to folder (same created above)
    try:
        cv2.imwrite(r"C:\Users\Majid Alnujaidi\Desktop\ROI\4\picture%i.jpg" % i,
                resized_img)
    except Exception as e:
        continue

    cv2.imshow("img", resized_img)
    print("Done with image ", i)
    i += 1
    cv2.waitKey(30)


print(i, " images have been processed")
cv2.destroyAllWindows()

