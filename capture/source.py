#
#  source.py
#  capturePlate
#
#  Created by Komron Aripov on 21/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

import cv2

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def resolution(self):
        return self.width * self.height

    def tuple_params(self, width_first=True):
        """ Returns the window paramters as a tuple
        """
        if not width_first:
            return (self.height, self.width)

        return (self.width, self.height)


WINDOW = Window(width=300, height=200)


def show_webcam(mirror=False):

    cam = cv2.VideoCapture(0)

    while True:
        ret_val, img = cam.read()

        img = cv2.resize(img, WINDOW.tuple_params())

        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)

        cv2.startWindowThread()
        cv2.namedWindow('my webcam', cv2.WINDOW_NORMAL)

        if cv2.waitKey(1) == 27:
            break  # esc to quit


    cam.release()
    cv2.destroyAllWindows()



show_webcam(mirror=True)
