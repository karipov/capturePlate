#
#  main.py
#  capturePlate
#
#  Created by Komron Aripov on 23/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

from source import Window, Camera

RPI_IP_ADDR = "192.168.1.156"
RPI_PORT = "8081"

camera = Camera(width=400, height=267) # original: 800, 533
camera.show_feed()
