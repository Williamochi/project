import cv2

img = cv2.imread('lenna.jpg')
#img = cv2.imread('lenna.bmp')
cv2.imshow('window',img)
cv2.waitKey(0)