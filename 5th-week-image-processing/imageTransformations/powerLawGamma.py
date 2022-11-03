import cv2
import numpy as np


img = cv2.imread('gammaImg.jpg', cv2.IMREAD_UNCHANGED)

# Apply Gamma=2.2
gamma_1 = np.array(255*(img/255)**2.2,dtype='uint8')

# Apply Gamma=0.4 
gamma_2 = np.array(255*(img/255)**0.4,dtype='uint8')

img3 = cv2.hconcat([gamma_1,gamma_2])
cv2.imshow('gammaImg', img3)
cv2.waitKey(0)