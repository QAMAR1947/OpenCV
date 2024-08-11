import cv2
import numpy as np

# Load the image
image = cv2.imread("resources/test2.png")

# Resize the image
resize_image = cv2.resize(image, (500, 500))

# Blur the image
blur_image = cv2.GaussianBlur(resize_image, (11, 11), 0)

# Convert to grayscale
gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert the combined sobel result to 8-bit image
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# Canny Edge Detector
img_edge = cv2.Canny(resize_image, 51, 51)
# Thickness of lines
mat_kernal = np.ones((3, 3), np.uint8)
dilated_image = cv2.dilate(sobel_combined, mat_kernal, iterations=1)

# Make thinner outline
ero_image = cv2.erode(dilated_image, mat_kernal, iterations=1)

# Crop image (height, width)
crop_image = resize_image[0:350, 150:500]

# Display images
cv2.imshow("Original Image", resize_image)
# cv2.imshow("Blur Image", blur_image)
cv2.imshow("Edge Image (Sobel)", sobel_combined)
cv2.imshow("Edge Image (Canny)", img_edge)
cv2.imshow("Dilated Image", dilated_image)
# cv2.imshow("Erosion Image", ero_image)
# cv2.imshow("Cropped Image", crop_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
