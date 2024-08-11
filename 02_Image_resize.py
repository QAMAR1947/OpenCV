import cv2
import numpy as np

# loading image
img = cv2.imread("resources/sample.jpg")

# checking dimensions of image
print("orignal image shape", img.shape)

# resizing image
resized_image = cv2.resize(img, (900, 700))
print("resized image shape", resized_image.shape)

# display image
cv2.imshow("orignal image", img)
cv2.imshow("resized image", resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
