import cv2
import time
RUNNING = True

video = cv2.VideoCapture(0)
time.sleep(1)

while RUNNING:
    check, frame = video.read()
    cv2.imshow('My Video', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        RUNNING = False

video.release()
