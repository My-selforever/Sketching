import imageio
import numpy as np
import cv2
import scipy.ndimage
import os

os.system('cls')



def gray(img):
    return np.dot(img[...,:3],[0.2989,0.5870,0.1140])

def sketch(bimg,gimg):
    finalSketch = bimg*255/(255-gimg)
    finalSketch[finalSketch>255] = 255
    finalSketch[gimg == 255] = 255
    return finalSketch.astype('uint8')

MyIMg = imageio.imread('me.jpg')

grayimage = gray(MyIMg)

i = 255-grayimage

blurimg = scipy.ndimage.filters.gaussian_filter(i,sigma=15)
Final = sketch(blurimg,grayimage)
cv2.imshow('Sketch',Final)
cv2.waitKey(0)