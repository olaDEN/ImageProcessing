import cv2

image = cv2.imread('Noise_image.png')

img = cv2.medianBlur(image,5) # kernel size 5
img3 = cv2.hconcat([image,img])
cv2.imshow('result', img3)
cv2.waitKey(0)
