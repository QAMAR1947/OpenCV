import cv2

video = cv2.VideoCapture("resources/videotest.mp4")

# indicator
if(video.isOpened() == False):
    print("couldn't read your video")

# reading and playing
while(video.isOpened):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break;
    else:
        break;

video.release()
cv2.destroyAllWindows()