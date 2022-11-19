import cv2
import numpy as np


img = cv2.imread('images\\gammaImg.jpg', cv2.IMREAD_UNCHANGED)

# Gamma=3.0
gamma3 = np.array(255*(img/255)**3.0,dtype='uint8')

# Gamma=4.0 
gamma4 = np.array(255*(img/255)**4.0,dtype='uint8')

# Gamma=5.0 
gamma5 = np.array(255*(img/255)**5.0,dtype='uint8')

result = cv2.hconcat([gamma3,gamma4,gamma5])
cv2.namedWindow('gammaImg', cv2.WINDOW_NORMAL)
cv2.imshow('gammaImg', result)
cv2.waitKey(0)