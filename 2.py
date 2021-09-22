from Sketch import gray
import cv2
import scipy.ndimage

img = cv2.imread('AOT.jpg')
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


i = 255-grayimg

blurimg = scipy.ndimage.filters.gaussian_filter(i,sigma=30)

cv2.imshow('hi',blurimg)
cv2.waitKey(0)