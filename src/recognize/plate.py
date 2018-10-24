#
#  plate.py
#  capturePlate
#
#  Created by Komron Aripov on 24/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

import cv2
from ..capture.source import Window, Camera
from ..capture.unwrap import Unwrap

# original camera resolution
# camera = Camera(width=400, height=267)

config = Unwrap(mode="HOME")
camera = Camera(width=640, height=480, source=config.url)

while camera.view.isOpened():
    ret_val, frame = camera.view.read()
    frame = cv2.resize(frame, (camera.width, camera.height))

    cv2.imshow(camera.name, frame)
    cv2.startWindowThread()
    cv2.namedWindow(camera.name, cv2.WINDOW_NORMAL)

    # q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
