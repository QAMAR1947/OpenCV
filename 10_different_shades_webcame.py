# importing libraries
import cv2

# initializing webcame
cap = cv2.VideoCapture(0)

while(cap.isOpened() == True):
    ret, frame = cap.read()
    # converting to grayscale
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # converting to black and white
    threshold, binary = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)

    if ret == True:
        cv2.imshow('orignal', frame)
        cv2.imshow("grayScale", grayScale)
        cv2.imshow("Binary", binary)
        # for quiting with 'q' key
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()