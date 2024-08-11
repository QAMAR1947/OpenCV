import cv2
import numpy as np

video = cv2.VideoCapture(0)

# sd resolution
def sd_resolution():
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# hd resolution
def hd_resolution():
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# full_hd resolution
def fhd_resolution():
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# setting FPS of video
def fps():
    video.set(cv2.CAP_PROP_FPS, 30)

sd_resolution()
# hd_resolution()
# fhd_resolution()
fps()

while (video.isOpened() == True):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break;
    else:
        break;
        
video.release()
cv2.destroyAllWindows()