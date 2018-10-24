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
        """ Returns number of pixels
        """
        return self.width * self.height

    def tuple_params(self, width_first: bool = True) -> (int, int):
        """ Returns the window paramters as a tuple
        """
        if not width_first:
            return (self.height, self.width)

        return (self.width, self.height)


class Camera(Window):
    def __init__(self,
                 width: int,
                 height: int,
                 source: str = 0,
                 name: str = "window"):

        super().__init__(width, height, name)
        self.view = self._setup_feed(source=source)

    def _setup_feed(self,
                   source: any = 0,
                   mirror: bool = False):
        """ Returns the cv2 camera object
        """

        cam = cv2.VideoCapture(source)
        return cam

    def show_feed(self, source: any = 0, mirror: bool = False):
        """ Displays a window with live camera feed
        """
        cam = cv2.VideoCapture(source)

        while cam.isOpened():
            ret_val, frame = cam.read()
            frame = cv2.resize(frame, (self.width, self.height))

            if mirror:
                frame = cv2.flip(frame, 1)

            cv2.imshow(self.name, frame)
            cv2.startWindowThread()
            cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)

            if cv2.waitKey(1) == 27:
                break  # esc to quit

        cam.release()
        cv2.destroyAllWindows()
