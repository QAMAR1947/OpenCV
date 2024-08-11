 # importing libraries
import numpy as np
import cv2

# def function of coordinates
def get_coordinates(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # left mouse click
        print(x, "", y)
        # how to define or print on the same image
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(scale_f_down, str(x) + ',' + str(y), (x, y), font, 1, (0, 0, 255), thickness=2)
        # show the text on the image and image itself
        cv2.imshow('scale-down', scale_f_down)

    # getting the color co_ordinate
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, "", y)
        # getting color co-ordinates using color channels 
        font = cv2.FONT_HERSHEY_PLAIN
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        
        cv2.putText(scale_f_down, str(b)+ ',' + str(g)+ ',' + str(r), (x, y), font, 1, (255, 255, 255), thickness=1)
        # displaying image
        cv2.imshow("scale-down", scale_f_down)

if __name__ == "__main__":
    # reading the image
    img = cv2.imread('resources/testimage2.jpg')

    # resizing image
    # print(img.shape)
    # h, w, c = img.shape
    # print("height:",h,"width:", w,"channel:", c)

    scale_down = 1

    scale_f_down = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)

    # display the image
    # cv2.imshow('image', img)
    cv2.imshow("scale-down", scale_f_down)
    # calling the function
    cv2.setMouseCallback('scale-down', get_coordinates)

    cv2.waitKey(0)
    cv2.destroyAllWindows()