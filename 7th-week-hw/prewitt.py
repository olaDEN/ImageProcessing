import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images\\gammaImg.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)


kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(img_prewittx, cmap = 'gray')
plt.title('prewitt X')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(img_prewitty, cmap = 'gray')
plt.title('prewitt Y')
plt.xticks([]), plt.yticks([])

plt.show()
