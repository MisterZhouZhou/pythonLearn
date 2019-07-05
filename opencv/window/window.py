# coding:utf-8
import cv2

img = cv2.imread('../images/82.jpg')
cv2.namedWindow('enhanced', 0)
cv2.resizeWindow('enhanced', 640, 480)
cv2.imshow('enhanced', img)
cv2.waitKey(0)