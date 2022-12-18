import cv2 
 
imgGray = cv2.imread("rgbImg.jpg", cv2.IMREAD_GRAYSCALE)

imgColorSpr= cv2.applyColorMap(imgGray, cv2.COLORMAP_SPRING)
imgColorSumm= cv2.applyColorMap(imgGray, cv2.COLORMAP_SUMMER)
imgColorAut = cv2.applyColorMap(imgGray, cv2.COLORMAP_AUTUMN)
imgColorWint= cv2.applyColorMap(imgGray, cv2.COLORMAP_WINTER)
imgColorOc = cv2.applyColorMap(imgGray, cv2.COLORMAP_OCEAN)
imgColorCo = cv2.applyColorMap(imgGray, cv2.COLORMAP_COOL)
imgColorJet = cv2.applyColorMap(imgGray, cv2.COLORMAP_JET)
imgColorBone = cv2.applyColorMap(imgGray, cv2.COLORMAP_BONE)

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
img3 = cv2.hconcat([imgColorSpr, imgColorSumm,imgColorAut, imgColorWint, imgColorOc, imgColorCo, imgColorJet, imgColorBone])
cv2.imshow('result', img3)
cv2.waitKey(0)
