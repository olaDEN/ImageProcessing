import cv2
import numpy as np


img = cv2.imread('imageNeg.jpg')

# Apply log transform
img_log = (np.log(img+1)/(np.log(1+np.max(img))))*255

# Specify data type
img_log = np.array(img_log,dtype=np.uint8)
 
img3 = cv2.hconcat([img, img_log])
cv2.imshow('log_image',img3 )
cv2.waitKey(0)
# cv2.destroyAllWindows ()

