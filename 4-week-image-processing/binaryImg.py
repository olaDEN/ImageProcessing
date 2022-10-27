import cv2
import numpy as np



# Binary Image:
h = 300
w = 300
img = np.random.randint(255, size= (h, w, 1), dtype = np.uint8)
cv2.imshow('Binary', img)
cv2.waitKey()
cv2.destroyAllWindows()
