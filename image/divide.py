import cv2


def divfunc(src):
    img = cv2.imread(src)

    # cv2.imread() -> takes an image as an input
    h, w, channels = img.shape

    half = w//2


    # this will be the first column
    left_part = img[:, :half]

    # [:,:half] means all the rows and
    # all the columns upto index half

    # this will be the second column
    right_part = img[:, half:]

    # [:,half:] means all the rows and all
    # the columns from index half to the end
    # cv2.imshow is used for displaying the image
    # cv2.imshow('Left part', left_part)
    # cv2.imshow('Right part', right_part)

    # cv2.imshow('Top', top)
    # cv2.imshow('Bottom', bottom)

    # saving all the images
    # cv2.imwrite() function will save the image
    # into your pc

    cv2.imwrite(src[:-4]+'right.png', right_part)
    cv2.imwrite(src[:-4]+'left.png', left_part)
    print(src[6:-4]+'left.png')
    return src[:-4]+'left.png', src[:-4]+'right.png'
