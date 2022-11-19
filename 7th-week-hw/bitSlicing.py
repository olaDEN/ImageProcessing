import cv2

img = cv2.imread('images\\Broadway_tower_grayscale.jpg')

# 8 bit
imgs = [255 * ((img & (1<<i)) >>i) for i in range(8)]
cv2.imwrite('results\\slices\\bsp_1.jpg',imgs[0])
cv2.imwrite('results\\slices\\bsp_2.jpg',imgs[1])
cv2.imwrite('results\\slices\\bsp_3.jpg',imgs[2])
cv2.imwrite('results\\slices\\bsp_4.jpg',imgs[3])
cv2.imwrite('results\\slices\\bsp_5.jpg',imgs[4])
cv2.imwrite('results\\slices\\bsp_6.jpg',imgs[5])
cv2.imwrite('results\\slices\\bsp_7.jpg',imgs[6])
cv2.imwrite('results\\slices\\bsp_8.jpg',imgs[7])

img8 = cv2.imread('results\\slices\\bsp_8.jpg')
#16 bit
imgs16 = [255 * ((img8 & (1<<i)) >>i) for i in range(8)]
cv2.imwrite('results\\slices\\bsp_9.jpg',imgs16[0])
cv2.imwrite('results\\slices\\bsp_10.jpg',imgs16[1])
cv2.imwrite('results\\slices\\bsp_11.jpg',imgs16[2])
cv2.imwrite('results\\slices\\bsp_12.jpg',imgs16[3])
cv2.imwrite('results\\slices\\bsp_13.jpg',imgs16[4])
cv2.imwrite('results\\slices\\bsp_14.jpg',imgs16[5])
cv2.imwrite('results\\slices\\bsp_15.jpg',imgs16[6])
cv2.imwrite('results\\slices\\bsp_16.jpg',imgs16[7])


img16 = cv2.imread('results\\slices\\bsp_16.jpg')
# 24 bit
imgs24 = [255 * ((img16 & (1<<i)) >>i) for i in range(8)]
cv2.imwrite('results\\slices\\bsp_17.jpg',imgs24[0])
cv2.imwrite('results\\slices\\bsp_18.jpg',imgs24[1])
cv2.imwrite('results\\slices\\bsp_19.jpg',imgs24[2])
cv2.imwrite('results\\slices\\bsp_20.jpg',imgs24[3])
cv2.imwrite('results\\slices\\bsp_21.jpg',imgs24[4])
cv2.imwrite('results\\slices\\bsp_22.jpg',imgs24[5])
cv2.imwrite('results\\slices\\bsp_23.jpg',imgs24[6])
cv2.imwrite('results\\slices\\bsp_24.jpg',imgs24[7])

result = cv2.hconcat([cv2.imread('images\\Broadway_tower_grayscale.jpg'),cv2.imread('results\\slices\\bsp_8.jpg'),cv2.imread('results\\slices\\bsp_16.jpg'), cv2.imread('results\\slices\\bsp_24.jpg')])

# Display the images
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result',result)
cv2.waitKey(0) 