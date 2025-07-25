"""
## Introduction
The "Movement Data Logger" project involves using the accelerometer sensor on the micro:bit to capture and log movement data. 
Your movement style is recorded and it's respective labels displays in real-time on the micro:bit's LEDs. 
The programming concepts utilized include decorators, functions, and a continuous loop.

## Parts of the Micro:bit Used
Accelerometer Sensor: Detects changes in movement along the X, Y, and Z axes.
LEDs (Light Emitting Diodes): Displays the respective labels for the real-time movement data.

## Programming Concepts
Decorators: Used to set up a periodic task to log accelerometer data at regular intervals.
Functions: Defined functions to log movement data and display it on the micro:bit.
While Loop: Ensures continuous execution of the program.

## Programming Language
 Python

## Coding Environment / Text Editor
   micro:bit python editor(https://python.microbit.org/v/3)

## Feel free to comment or contribute

"""


## Project code / program
from microbit import *
import log


@run_every(s=1) # data should be recorded every 1 second

#X-tilting from left to right .(LR)
#Y-tolting forward and backwards.(FB)
#Z-moving up and down(UD)


def log_data():
    log.add({ 
        'X':accelerometer.get_x() ,
        'y':accelerometer.get_y() ,
        'z':accelerometer.get_z()
    })

# code in a 'while true:' loop repeats forever
while True:
     x = accelerometer.get_x()
     if x == x :
         display.scroll('LR')
     y = accelerometer.get_y()
     if y == y :
         display.scroll('FB')
     z = accelerometer.get_z()
     if z == z :
         display.scroll('UD')
