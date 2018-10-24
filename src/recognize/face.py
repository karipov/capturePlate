#
#  face.py
#  capturePlate
#
#  Created by Komron Aripov on 24/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

from os.path import dirname, join
from ..capture.source import Window, Camera
from ..capture.unwrap import Unwrap
import cv2

# original camera resolution
# camera = Camera(width=400, height=267)

config = Unwrap(mode="HOME")
camera = Camera(width=640, height=480, source=config.url)

project_dir = dirname(dirname(__file__))
face_cascade_path = join(project_dir, "haarcascades/haarcascade_frontalface_default.xml")
eye_cascade_path = join(project_dir, "haarcascades/haarcascade_eye.xml")

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

while camera.view.isOpened():
    ret_val, frame = camera.view.read()
    frame = cv2.resize(frame, (camera.width, camera.height))


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255, 0), 2)



    cv2.imshow(camera.name, frame)
    cv2.startWindowThread()
    cv2.namedWindow(camera.name, cv2.WINDOW_NORMAL)

    # q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
