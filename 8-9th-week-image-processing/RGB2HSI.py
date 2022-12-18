import cv2

img = cv2.imread('rgbImg.jpg')

hsvImg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

rgbImg = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2RGB)

img3 = cv2.hconcat([img,hsvImg,rgbImg])
cv2.imshow('rgb2hsi & hsi2rgb', img3)
cv2.waitKey(0)