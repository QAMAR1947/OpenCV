import cv2

orignal_image = cv2.imread("resources/test2.png")
gray_image = cv2.cvtColor(orignal_image, cv2.COLOR_BGR2GRAY)
threshold, binary = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Car", orignal_image)
cv2.imshow("Gray", gray_image)
cv2.imshow("Binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()