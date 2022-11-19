import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images\\imageNeg.jpg')

# image to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# image to gray-scale also
gray = cv2.imread('images\\imageNeg.jpg', 0)

# Getting image's negatives
colored_negative = cv2.bitwise_not (img)
 
gray_negative = cv2.bitwise_not (gray)


images = [img, gray, colored_negative, gray_negative]
titles = ['Original', 'Gray-Scale', 'Coloured-Negative', 'Gray-Negative']


plt.subplot(2, 2, 1)
plt.title(titles[0])
plt.imshow(images[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.title(titles[1])
plt.imshow(images[1], cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.title(titles[2])
plt.imshow(images[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.title(titles[3])
plt.imshow(images[3], cmap='gray')
plt.xticks([])
plt.yticks([])
cv2.waitKey(0)
plt.show()