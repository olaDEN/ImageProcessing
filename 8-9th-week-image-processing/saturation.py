import cv2
from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt

img = Image.open('rgbImg.jpg')
saturated = ImageEnhance.Color(img)
saturatedImg = saturated.enhance(3.0)
saturatedImg.save("saturatedImg.jpg")

imgGray = cv2.imread('rgbImg.jpg',0)
SaturatedGray = cv2.imread('saturatedImg.jpg',0)

# find frequency of pixels in range 0-255
histrBefore = cv2.calcHist([imgGray],[0],None,[256],[0,256])
histrAfter = cv2.calcHist([SaturatedGray],[0],None,[256],[0,256])

plt.subplot(1,2, 1)
plt.title('Before')
plt.plot(histrBefore)


plt.subplot(1, 2, 2)
plt.title('After')
plt.plot(histrAfter)

plt.show()