import cv2
import glob
import os

# Resize + Crop images in folder

# Folder where images are
inputFolder = r"C:\Users\Majid Alnujaidi\Desktop\testcrop copy"

# Create a folder to save images in (will not override if folder exists)
os.mkdir(r"C:\Users\Majid Alnujaidi\Desktop\testcrop copy\cropped and resized")


i=0
for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    imgResize = cv2.resize(image, (900, 600))
    roi = imgResize[150:450,275:625]
    # Write to matching directory made above
    cv2.imwrite(r"C:\Users\Majid Alnujaidi\Desktop\testcrop copy\cropped and resized\image%i.jpg" % i,
                roi)
    i += 1
    cv2.imshow('image', roi)
    cv2.waitKey(30)

cv2.destroyAllWindows()