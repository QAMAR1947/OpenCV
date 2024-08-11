import cv2 

cap = cv2.VideoCapture("resources/video1.mp4")

frameNumber = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite(f"resources/frames/frame_{frameNumber}.jpg", frame)
    else:
        break;
    frameNumber += 2
cap.release()