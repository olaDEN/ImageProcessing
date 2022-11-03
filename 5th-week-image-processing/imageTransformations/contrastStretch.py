import cv2
import numpy as np
  
# Map each intensity level.
def pixVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
  

img = cv2.imread('image.jpg')
  
# Function parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
# Vectorize function to apply it to value in the array.
pixelVal_vec = np.vectorize(pixVal)
  
# contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
  
cv2.imshow('Original', img)
cv2.imshow('contrast_stretch', contrast_stretched)
cv2.waitKey(0)