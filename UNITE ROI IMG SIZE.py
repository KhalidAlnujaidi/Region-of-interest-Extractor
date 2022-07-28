import glob
import os
import cv2
import numpy as np



# Folder where images are located
inputFolder = r"C:\Users\Majid Alnujaidi\Desktop\ROI\4"
# Create a folder to save images in (will not override if folder exists)
os.mkdir(r"C:\Users\Majid Alnujaidi\Desktop\ROI_similar_sizes\4")

# counter to name images
i = 1

# Travers all images in directory
for img in glob.glob(inputFolder + "/*.jpg"):
    # read image
    raw_img = cv2.imread(img)

    # width missing to make image 350 width
    width_diff = abs(500.0 - raw_img.shape[1])
    # percentage needed to increase the image size
    percentage_needed_to_change = (width_diff / 500.0) * 100

    # Resize and Preserve Aspect Ratio
    scale_percent = 100 + (percentage_needed_to_change)
    width = int(raw_img.shape[1] * scale_percent / 100)
    height = int(raw_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv2.resize(raw_img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow('raw', resized_img)

    # Save the image to folder (same created above)
    try:
        cv2.imwrite(r"C:\Users\Majid Alnujaidi\Desktop\ROI_similar_sizes\4\picture%i.jpg" % i,
                    resized_img)
    except Exception as e:
        continue

    cv2.imshow("img", resized_img)
    print("Done with image ", i)
    i += 1
    cv2.waitKey(30)





print(i, " images have been processed")
cv2.destroyAllWindows()
