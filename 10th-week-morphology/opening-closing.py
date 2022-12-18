import cv2
import numpy as np

image = cv2.imread("text.jpg")

filter = np.ones((9, 9), np.uint8)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, filter)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, filter)

cv2.namedWindow("openinngANDclosing", cv2.WINDOW_NORMAL)
result = cv2.hconcat([image,opening, closing])
cv2.imshow('openinngANDclosing', result)
cv2.waitKey(0)

