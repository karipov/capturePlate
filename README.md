# capturePlate
Project _capturePlate_ is an ALPR system used for keeping track of parked vehicles.

## Prerequisites
Make sure you have all the proper libraries installed with the following command
```
pip3 install -r requirements.txt
```

## How to run python code
Currently, to run the program, move to the _capturePlate_ directory and run the following command to ensure that all the scripts are loaded correctly:
```
python -m src.recognize.plate
```
Also momentarily, there is a face recognition file that when run, can detect faces and eyes. To run, enter:
```
python -m src.recognize.face
```

## Scripts for the Raspberry Pi
To make sure that all dependencies are installed correctly, run the following while in the _capturePlate_ directory:
```
bash scripts/startup.sh
```
A script has also been included for easy camera startup. To run, enter:
```
bash scripts/motion.sh
```

## Notice
Project _capturePlate_ is still in its alpha stage. ALPHA = FEATURES MAY NOT WORK.
