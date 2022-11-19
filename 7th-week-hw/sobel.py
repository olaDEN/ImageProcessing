import cv2
from matplotlib import pyplot as plt

image = cv2.imread('images\\gammaImg.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get red of noise
img = cv2.GaussianBlur(img_gray,(3,3),0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X')
plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])

plt.show()