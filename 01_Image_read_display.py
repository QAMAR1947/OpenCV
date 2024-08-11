import cv2
import numpy as np

# loading image
img = cv2.imread("resources/test.jpg")
# display image
cv2.imshow("myImage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
