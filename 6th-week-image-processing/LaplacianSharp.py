import cv2

# Load the image in greyscale
img = cv2.imread('smoothimg.jpg',cv2.IMREAD_COLOR)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(3,3),0)

gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(gray,ddepth=cv2.CV_16S,ksize=3)

convert = cv2.convertScaleAbs(laplacian)

cv2.namedWindow('Laplacian', cv2.WINDOW_AUTOSIZE)

cv2.imshow('Laplacian',convert)
cv2.waitKey(0)