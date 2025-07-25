"""
## Introduction

Curious about how many steps you take? This project turns your micro:bit into a pedometer, counting your steps as you move. 

You'll explore the accelerometer sensor, buttons, and LEDs while applying programming concepts like functions, variables, and global variables.


## Parts of the Micro:bit

1. **Accelerometer Sensor:** Detects motion and measures acceleration.
2. **LEDs (Light Emitting Diode):** Displays step count information.
3. **Buttons:** Input for interaction with the micro:bit.


## Programming Concepts

 **Function:** A reusable block of code that performs a specific task. Functions will be used to handle step counting and display.
 **Variable:** A container for storing data. Variables will be employed to keep track of the step count.
 **Global Variable:** A variable that can be accessed from anywhere in the program.


## Programming Language

   Python


## Coding Environment / Text Editor

- [Microsoft MakeCode Editor](https://makecode.microbit.org/#editor)


## Feel free to comment or contribute

"""




# Project Code / Program ...

steps = 0  # Initialize a variable to count steps


def on_gesture_shake(): # Define a function to increment the step count and display it when the micro:bit is shaken
    global steps
    steps += 1
    basic.show_number(steps)


input.on_gesture(Gesture.SHAKE, on_gesture_shake) # An event handler for the shake gesture
