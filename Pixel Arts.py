"""
## Introduction
   Turn your cool pixel drawings into magical light shows! After crafting your pixel arts with paper, use this micro:bit project code below to make them glow and shine. 
   It's like adding a spark of magic to your artwork! 🌟"

 ## Parts of the micro:bit used
   Pins: Connected to external LEDs for illuminating or light up the pixel art

## Programming concepts
   Functions are  reusable code that perform a specific task or set of tasks. Eg: Line 24, 28

## Programming language
   Python

## Coding environment or text editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

"""

## Project code / program

def on_button_pressed_a():  # Define a function to be executed when button A is pressed
  pins.digital_write_pin(DigitalPin.P0, 1)    # Turn on the digital output pin P0 when button A is pressed
input.on_button_pressed(Button.A, on_button_pressed_a)  # Set up an event handler for button A

def on_button_pressed_b():  # Define a function to be executed when button B is pressed
  pins.digital_write_pin(DigitalPin.P0, 0)     # Turn off the digital output pin P0 when button B is pressed
input.on_button_pressed(Button.B, on_button_pressed_b)  # Set up an event handler for button B
