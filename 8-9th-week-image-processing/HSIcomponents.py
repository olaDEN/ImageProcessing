import numpy as np
import cv2

img = cv2.imread("spring.jpg", 1)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

cv2.imshow("Split HSV",hsv_split) # Hue, Saturation, Intensity
cv2.waitKey(0)
cv2.destroyAllWindows()