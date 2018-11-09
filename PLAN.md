## Goal:
To make a system to give information about:
- how many cars enter the school daily, monthly, year, for any timeframe
- their average duration of stay in the parking lot for a given day, month, year, for any timeframe
- the number (and license plate number) of all cars currently in the parking lot


## Overview:
The _raspberry_ is going to serve as the front-end for the project. It will broadcast a live video feed over an RTSP connection.
A _server_ is going to be the back-end of the project. It will do the recognition of the license plate, and fill in the database given the video feed captured by the _raspberry_


## Steps:
1. _raspberry_ captures the feed and broadcasts it over an IP connection @ entrance

2. _server_ receives the feed from a URL over an internet connection

3. _server_ works on plate recognition using either ALPR or a homemade solution involving ML and OpenCV
  1. Motion detection is first utilised to process the image only when and if it's moving
  2. OpenCV detects the region of interest (i.e. the license plate)
  3. OpenCV does some image processing (i.e. thresholding, dilution, erosion)
  4. OpenCV saves the file to a destination folder for PyTesseract
  5. possibly using PIL, the image is read as soon as it's added to the destination folder
  6. PyTesseract is used to recognise the characters, and the values are returned

4. _server_ enters the plate data into a database along with time (possibly a snapshot of the plate)

5. _raspberry_ captures the feed over an RTSP connection @ exit

6. _server_ retrieves plate information and time from the database

7. _server_ calculates information as according to the goal
