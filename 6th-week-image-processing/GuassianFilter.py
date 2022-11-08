import cv2

img = cv2.imread('flowers.jpeg')

result1 = cv2.GaussianBlur(img,(5,5),0)

result = cv2.hconcat([img, result1])

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', result)

cv2.waitKey(0)