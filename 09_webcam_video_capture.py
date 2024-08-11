# importing libraries
import cv2

# reading from webcame
cap = cv2.VideoCapture(0)

# checking if the camera is opened
if (cap.isOpened() == False):
    print("Not capturing")
else:
    print("Capturing...")

# capturing the frames
while(cap.isOpened()):
    ret, frame = cap.read()
    # showing the frames
    if(ret == True):
        cv2.imshow('frame', frame)
        # to quit with 'q' key
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()