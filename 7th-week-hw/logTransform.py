import cv2
import numpy as np

# gray image
img = cv2.imread('images\\imageNeg.jpg', 0)

# log transform
img_log = (np.log(img+1)/(np.log(1+np.max(img))))*255

img_log = np.array(img_log,dtype=np.uint8)
 
result = cv2.hconcat([img, img_log])
cv2.imshow('logImage',result)
cv2.waitKey(0)


