import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

img = cv.imread('image.jpg',0)

# show original image
fig = plt.figure()
fig.add_subplot(221)
plt.title('1- Original image ')
plt.set_cmap('gray')
plt.imshow(img)

# Histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
fig.add_subplot(222)
plt.title('2- Histogram ')
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

# Histogram equalized image
equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imwrite('histogramEqu.png',res)
fig.add_subplot(223)
plt.title('3-Histogram Equalization')
image = mpimg.imread('histogramEqu.png')
plt.imshow(image)

# Clahe: (Contrast Limited Adaptive Histogram Equalization).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res2 = np.hstack((img,cl1))
cv.imwrite('clahe.jpg',res2)
fig.add_subplot(224)
plt.title('4-Clahe:global histogram equalization')
image2 = mpimg.imread('clahe.jpg')
plt.imshow(image2)

plt.show()