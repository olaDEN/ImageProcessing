import cv2

img = cv2.imread('gammaImg.jpg')
imgs = [255 * ((img & (1<<i)) >>i) for i in range(8)]

cv2.imwrite('slices\\bsp_1.jpg',imgs[0])
cv2.imwrite('slices\\bsp_2.jpg',imgs[1])
cv2.imwrite('slices\\bsp_3.jpg',imgs[2])
cv2.imwrite('slices\\bsp_4.jpg',imgs[3])
cv2.imwrite('slices\\bsp_5.jpg',imgs[4])
cv2.imwrite('slices\\bsp_6.jpg',imgs[5])
cv2.imwrite('slices\\bsp_7.jpg',imgs[6])
cv2.imwrite('slices\\bsp_8.jpg',imgs[7])

result = cv2.hconcat([cv2.imread('slices\\bsp_8.jpg'),cv2.imread('slices\\bsp_7.jpg'),cv2.imread('slices\\bsp_6.jpg'),cv2.imread('slices\\bsp_5.jpg'),cv2.imread('slices\\bsp_4.jpg'), cv2.imread('slices\\bsp_3.jpg'),cv2.imread('slices\\bsp_2.jpg'),cv2.imread('slices\\bsp_1.jpg')])

# Display the images
cv2.imshow('result',result)
cv2.waitKey(0) 