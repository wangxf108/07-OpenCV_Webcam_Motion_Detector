# Write a script that resizes all images in a directory to 100x100. 

import cv2
import glob    # Globae library will find all the files in a certain pattern.

images=glob.glob("*.jpg")    # find all the jpg files in the file.

for image in images:
    img=cv2.imread(image,0)       # first, read the files. 0 means that a image should be read as black and white.
    re=cv2.resize(img,(100,100))  # resize the images
    cv2.imshow("Hey",re)          # Hey, the new of the image.
    cv2.waitKey(500)              # 500 it will show 500 milliseconds.
    cv2.destroyAllWindows()       #
    cv2.imwrite("resized_"+image,re)   # new name of the file