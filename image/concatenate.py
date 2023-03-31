# import cv2 library
import cv2
from image.aes import *

def concatfunc(src1, src2):
    # read the images
    img1 = cv2.imread(src1)
    img2 = cv2.imread(src2)
    # horizontally concatenates images
    # of same height
    im_h = cv2.hconcat([img1, img2])

    # show the output image
    cv2.imwrite("media/joined.png" , im_h)
