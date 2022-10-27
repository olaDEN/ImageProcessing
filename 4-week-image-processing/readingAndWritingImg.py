import cv2

# Reading and writing images :
img1 = cv2.imread("4-week-image-processing/cat.jpg")
cv2.imshow("Cat", cv2.resize(img1, (960, 540))) # resize for displaying the whole picture if it is too big
# Size of the image:
print('\nimage size: ', img1.size)
# Data type of the image:
print('\nimage data type: ', img1.dtype)
# Dimension of the image and number of channels:
print('\nimage shape: ', img1. shape)
cv2.waitKey()
cv2.destroyAllWindows()