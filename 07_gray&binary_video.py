import cv2

# reading video
orignal_video = cv2.VideoCapture("resources/video1.mp4")

while(orignal_video.isOpened):
    ret, frame = orignal_video.read()

    # converting into grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # converting into binary video
    threshold, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

    # to show in player
    if(ret == True):
        # cv2.imshow("orignalVideo", frame)
        # cv2.imshow("grayVideo", grayscale)
        cv2.imshow("BinaryVideo", binary)

        # to quit with 'q' key
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break;
    else:
        break;