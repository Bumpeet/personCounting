'''
This file helps you in choosing the co-ordinates of your reference line.
Run this file and click on the points of your choice and they will get printed on th console
'''

import cv2


def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x,y)

def main(src_path):
    cap = cv2.VideoCapture(src_path)

    while cap.isOpened():
        _, frame = cap.read()

        if cv2.waitKey(10)==ord('q'):
            break
        else:
            cv2.imshow("wid", frame)
            cv2.setMouseCallback("wid", mouse_callback)
            cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__=="__main__":
    src_path = "person.mp4" 
    main(src_path)


