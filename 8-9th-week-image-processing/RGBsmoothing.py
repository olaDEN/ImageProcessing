import cv2

img = cv2.imread('spring.jpg')

bl,gr,rd=cv2.split(img)

# 5*5 smoothing filter to each RGB component
blurBl = cv2.blur(bl,(5,5))
blurGr = cv2.blur(gr,(5,5))
blurRd = cv2.blur(rd,(5,5))

after = cv2.merge([blurBl, blurGr, blurRd])
before = cv2.hconcat([blurBl,blurGr,blurRd])

cv2.imshow('RGB', before)
cv2.imshow('SmoothedRGB', after)
cv2.waitKey(0)