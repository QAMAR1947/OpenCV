# importing libraries
import numpy as np
import cv2

# loading image
img = cv2.imread('resources/testimage2.jpg')
print(img.shape)
# h, w, c = img.shape
# print("height:",h,"width:", w,"channel:", c)

scale_down = 1
scale_f_down = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
h, w, c = scale_f_down.shape
print("scale-down-height:",h,"width:", w,"channel:", c)
# finding points 
point1 = np.float32([[264, 36], [735, 257], [22, 198], [526, 518]])
width = 700
height = 500
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(point1, point2)
output_image = cv2.warpPerspective(scale_f_down, matrix, (width, height))

# displaying image
# cv2.imshow('orignal image', img)
cv2.imshow("scale-down", scale_f_down)
cv2.imshow('transformed_image', output_image)
# cv2.imwrite("resources/out-persp2.jpeg", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()