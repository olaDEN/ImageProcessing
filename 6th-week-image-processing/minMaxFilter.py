from PIL import Image, ImageFilter
import cv2
import pylab as pylab
import matplotlib.pyplot as plt

# MaxFilter() for removing the pepper noise followed by a MinFilter() for removing the salt noise

original = Image.open(r"Noise_image.png")
   
max = original.filter(ImageFilter.MaxFilter(size = 3))

min = original.filter(ImageFilter.MinFilter(size = 3))

both = max.filter(ImageFilter.MinFilter(size = 3))

images = [original, max, min, both]
titles = ['Original', 'Max', 'Min', 'both']


plt.subplot(2, 2, 1)
plt.title(titles[0])
plt.imshow(images[0], cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.title(titles[1])
plt.imshow(images[1], cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.title(titles[2])
plt.imshow(images[2], cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.title(titles[3])
plt.imshow(images[3], cmap='gray')
plt.xticks([])
plt.yticks([])
cv2.waitKey(0)
plt.show()
