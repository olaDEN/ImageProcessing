import cv2
import numpy as np

image = cv2.imread("text.jpg")

filter = np.ones((9, 9), np.uint8)

image_ero = cv2.erode(image, filter)

image_di = cv2.dilate(image, filter, iterations=1)
cv2.namedWindow("erosionANDdialation", cv2.WINDOW_NORMAL)
result = cv2.hconcat([image,image_ero, image_di])
cv2.imshow('erosionANDdialation', result)
cv2.waitKey(0)

