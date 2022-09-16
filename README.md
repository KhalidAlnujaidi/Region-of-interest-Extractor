
## Extracting region of intrest within images

1.jpg

### RIO EXTRACTIOM.py :

First image is converted into gray scale

Then the use on Erosion, Dilation, and GaussianBlur to apply more accurite Canny

Image threshold is applied to find contours and find Bounding rectangle

Image is then cropped based on Bouding Rectangle +- 50pixles to leave some room around the images





### UNITE RIO IMG SIZE.py
Simple loop to resize all the images of extracted RIO into similar sizes in respect to thier original Aspect Ratio 


