import cv2

video = cv2.VideoCapture(0)

# hd_resolution
def hd_resolution():
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# calling function
hd_resolution()

# writing codecs for video
frame_width = int(video.get(3))
frame_height = int(video.get(4))
output = cv2.VideoWriter("resources/hdVideo.mp4", cv2.VideoWriter.fourcc(*"mpv4"), 30, (frame_width, frame_height))


while(video.isOpened() == True):
    ret, frame = video.read()
    if ret == True:
        output.write(frame)
        cv2.imshow("video", frame)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break;
    else:
        break;