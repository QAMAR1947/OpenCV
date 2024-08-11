import cv2
import numpy as np

# loading image
img = cv2.imread("resources/car1.jpg")

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# display image
# cv2.imshow("orignal image", img)
# cv2.imshow("grayScale image", grayscale)

# writing image
cv2.imwrite("resources/grayScaleCar.jpg", grayscale)

cv2.waitKey(0)

cv2.destroyAllWindows()
