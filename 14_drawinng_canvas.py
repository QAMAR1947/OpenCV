import cv2
import numpy as np

img = np.zeros((600, 600))
img1 = np.ones((600, 600))

print("The shape of image is: ", img.shape)
# colored image
color_image = np.zeros((600, 750, 3), np.uint8) # color channel addition
color_image[:] = (165, 190, 180)    # coloring complete image
# syntax (rows, cols) --> Parts of colored image
# color_image[180:400, 150:520] = (255, 255, 255)
# color_image[180:400, 280:520] = (0, 100, 0)

# displaying line --> (img, strt_point(width, height), end_point(width, height), color, thickness)
# cv2.line(color_image, (0, 300), (750, 300), (255, 0, 0), 3)
cv2.line(color_image, (color_image.shape[1], color_image.shape[0]), (0, 0), (0, 0, 255), 3)

# adding rectangle
cv2.rectangle(color_image, (370, 300), (750, 600), (255, 0, 0), 4)
cv2.rectangle(color_image, (0, 0), (370, 300), (220, 155, 0), cv2.FILLED)

# adding circle
cv2.circle(color_image, (180, 450), 120, (35, 34, 190), cv2.FILLED)
cv2.circle(color_image, (180, 150), 120, (35, 34, 190), 3)

# adding text
cv2.putText(color_image, "Cv2 Shapes", (380, 200), cv2.FONT_HERSHEY_COMPLEX, 1.5, (125, 55, 23))

# Displaying image
# cv2.imshow("Black", img)
# cv2.imshow("White", img1)
cv2.imshow("colored_image", color_image)


cv2.waitKey(0)
cv2.destroyAllWindows()