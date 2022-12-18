
import cv2
import numpy as np

img = cv2.imread('spring.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv)

# 5*5 smoothing filter to each RGB component
blurH = cv2.blur(h,(5,5))
blurS = cv2.blur(s,(5,5))
blurV = cv2.blur(v,(5,5))

after = cv2.merge([blurH, blurS, blurV])
before = cv2.hconcat([blurH,blurS,blurV])

cv2.imshow('HSI', before)
cv2.imshow('SmoothedHSI', after)
cv2.waitKey(0)
cv2.destroyAllWindows()