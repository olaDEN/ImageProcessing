import cv2

image = cv2.imread('rgbImg.jpg')

invert = 255 - image

img3 = cv2.hconcat([image,invert])
cv2.imshow("RGB Color Complement",img3)

cv2.waitKey(0)
