import cv2

video = cv2.VideoCapture(0)

# writing format, codec, video writer object and output
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
output = cv2.VideoWriter("resources/camOutput.mp4", cv2.VideoWriter.fourcc(*'mp4v'), 30, (frame_width, frame_height))

while(video.isOpened() == True):
    ret, frame = video.read()
    # converting into grayscale
    # grayVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # for displaying video in player
    if ret == True:
        output.write(frame)
        cv2.imshow('camVideo', frame)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break;
    else:
        break;

video.release()
output.release()
cv2.destroyAllWindows()