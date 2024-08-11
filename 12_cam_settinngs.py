import cv2

cap = cv2.VideoCapture(0)

cap.set(10, 100) # 10 is the key of brightness and other argument is conntrolling it
cap.set(3, 1080)
cap.set(4, 720)
# cap.set(11, 50)   # 11 key is for contrast
# cap.set(12, 200)  # 12 is for saturation
# cap.set(13, 200)  # 13 is for hue
# cap.set(14, 50)   # 14 is for gain
# cap.set(15, 50)   #15 is for exposure

while(cap.isOpened() == True):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("camVideo", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break

cap.release()
cv2.destroyAllWindows()