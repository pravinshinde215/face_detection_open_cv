import numpy as np
import cv2

cap = cv2.VideoCapture(0)
facedetection = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    gry = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = facedetection.detectMultiScale(gry,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 5)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()