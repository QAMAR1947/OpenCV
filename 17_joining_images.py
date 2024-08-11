import cv2
import numpy as np

img = cv2.imread("resources/test2.png")

# stacking same image
# horizontal stack
horizontal_stack = np.hstack((img, img))
# vertical stack
vertical_stack = np.vstack((img, img))

# cv2.imshow("image", img)
# cv2.imshow("hor_image", horizontal_stack)
cv2.imshow("vertical_stack", vertical_stack)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Considerations:
# Image Dimensions: Ensure that the images have the same dimensions along the axis of stacking. Use cv2.resize to adjust the size if needed.
# Data Types: Ensure that all images have the same data type and color channels.
# Aspect Ratio: When resizing images, maintain the aspect ratio to avoid distortion.