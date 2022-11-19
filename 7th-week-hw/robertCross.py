import cv2
import numpy as np
from scipy import ndimage

cross_v = np.array( [[1, 0 ],[0,-1 ]] )

cross_h = np.array( [[ 0, 1 ],[ -1, 0 ]] )

img = cv2.imread("images\\robert.webp",0).astype('float64')
img/=255.0
vert = ndimage.convolve( img, cross_v )
horiz = ndimage.convolve( img, cross_h )

img_edg = np.sqrt( np.square(horiz) + np.square(vert))
img_edg*=255

cv2.imwrite("results\\output.jpg",img_edg)

result = cv2.hconcat([cv2.imread("images\\robert.webp"), cv2.imread('results\\output.jpg')])
cv2.imshow('result', result)
cv2.waitKey(0)
