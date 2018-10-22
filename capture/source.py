#
#  source.py
#  capturePlate
#
#  Created by Komron Aripov on 21/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

import cv2

class Window():
    def __init__(self, width: int, height: int, name: str = "window"):
        self.width = width
        self.height = height
        self.name = name

    def resolution(self) -> (int):
        return self.width * self.height

    def tuple_params(self, width_first: bool = True) -> (int, int):
        """ Returns the window paramters as a tuple
        """
        if not width_first:
            return (self.height, self.width)

        return (self.width, self.height)


class Camera(Window):
    def __init__(self, width: int, height: int, name: str = "window"):
        super().__init__(width, height, name)

    def show_feed(self, mirror: bool = False):
        """ Displays a window with live camera feed
        """
        cam = cv2.VideoCapture(0)

        while True:
            ret_val, img = cam.read()
            img = cv2.resize(img, (self.width, self.height))

            if mirror:
                img = cv2.flip(img, 1)

            cv2.imshow(self.name, img)
            cv2.startWindowThread()
            cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)

            if cv2.waitKey(1) == 27:
                break  # esc to quit

        cam.release()
        cv2.destroyAllWindows()


camera = Camera(width=800, height=533)
camera.show_feed(mirror=True)
