
import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def resize(img):
    x = img.astype(np.float32)
    x -= x.min()
    x /= x.max()
    return x*255

img = cv2.imread('images\\blur_text.jpg',0)

gauss_filter = cv2.getGaussianKernel(ksize=19, sigma=3)
gauss_filter = np.dot(gauss_filter, gauss_filter.T)

blurred_img = signal.correlate2d(img, gauss_filter, mode="same")

mask = img - blurred_img 
mask = resize(mask)

# we can try different k values: 
k= 1
sharpened_img = img + k*mask 

k= 0.5
sharpened_img = img + k*mask 


plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.title('Original')

plt.subplot(132)
plt.imshow(sharpened_img, cmap="gray")
plt.title('k=1')

plt.subplot(133)
plt.imshow(sharpened_img, cmap="gray")
plt.title('k=0.5')

plt.show()