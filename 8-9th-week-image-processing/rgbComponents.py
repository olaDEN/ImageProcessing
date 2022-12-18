import cv2

img = cv2.imread('spring.jpg')

bl,gr,rd=cv2.split(img)

img3 = cv2.hconcat([rd,gr,bl])

cv2.imshow('rgbChannels', img3)
cv2.waitKey(0)