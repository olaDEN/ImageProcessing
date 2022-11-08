import numpy as np
import cv2

kernel1 = np.ones((9, 9),np.float32)/90
image = cv2.imread('Noise_image.png')
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
img3 = cv2.hconcat([image,img])
cv2.imshow('2DConvBlur', img3)
cv2.waitKey(0)
