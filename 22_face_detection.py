import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread("resources/facedetection.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect faces in the images
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Image", image)
cv2.imwrite("resources/faceDetectOutput.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()