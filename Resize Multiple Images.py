import cv2
import glob
import os

## Multiple image resize

## Folder where images are
inputFolder = r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\1"

## creat a folder to save images in
os.mkdir(r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\1\Class1reSized")

i = 0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    imgResize = cv2.resize(image, (900, 600))
    ## Write to matching directory made above
    cv2.imwrite(
        r"C:\Users\Majid Alnujaidi\Desktop\Date fruit diseases\phase 2\ImageData\1\Class1reSized\image%i.jpg" % i,
        imgResize)
    i += 1
    cv2.imshow('image', imgResize)
    cv2.waitKey(30)

cv2.destroyAllWindows()
