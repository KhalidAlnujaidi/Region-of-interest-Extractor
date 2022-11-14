
## Extracting region of intrest within images

This code was used to conduct to assist in the research titled "Date Fruit Disease Detection Using Machile Learning". The porpose of this code was to clean up the images and remove unnecessary / unrelated features from the image.

![example 1](1.jpg "Image Title")
![example 1](1x.jpg "Image Title")


![example 1](2.jpg "Image Title")
![example 1](2x.jpg "Image Title")

![process_of_RIO_extractor](https://user-images.githubusercontent.com/93127443/201628971-a1f8b48a-73b0-45c7-ac52-7396a741f80e.png)


### RIO EXTRACTIOM.py :

First image is converted into gray scale

Then the use on Erosion, Dilation, and GaussianBlur to apply more accurite Canny

Image threshold is applied to find contours and find Bounding rectangle

Image is then cropped based on Bouding Rectangle +- 50pixles to leave some room around the images





### UNITE RIO IMG SIZE.py
Simple loop to resize all the images of extracted RIO into similar sizes in respect to thier original Aspect Ratio 


