import cv2


image = cv2.imread('flowers.jpeg')

img1 = cv2.blur(image,(5,5))

# when ddepth=-1, the output image will have the same depth as the source.
img2 = cv2.boxFilter(image, -1, (2,2), normalize=True)

result = cv2.hconcat([image, img1, img2])

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', result)
cv2.waitKey(0)
