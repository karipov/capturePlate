## Goal:
To make a system to give information about:
- how many cars enter the school daily, monthly, year, for any timeframe
- their average duration of stay in the parking lot for a given day, month, year, for any timeframe
- the number (and license plate number) of all cars currently in the parking lot


## Overview:

The _raspberry_ is going to serve as the front-end for the project. It will broadcast a live video feed over an RTSP connection.
A _server_ is going to be the back-end of the project. It will do the recognition of the license plate, and fill in the database given the video feed captured by the _raspberry_


## Steps:
- _raspberry_ captures the feed over an RTSP connection @ entrance
- _server_ receives the RTSP feed from a URI over an internet connection
- _server_ works on plate recognition using either ALPR or a homemade solution involving ML and OpenCV
- _server_ enters the plate data into a database along with time (possibly a snapshot of the plate)
- _raspberry_ captures the feed over an RTSP connection @ exit
- _server_ retrieves plate information and time from the database
- _server_ calculates information as according to the goal
