## Introduction
   
    # Explore our Micro:bit-powered SDG Pixel Art PSA Cube. This is a fun program that allows you to control an external LED connected to GPIO pin P0 to flash or pulse or turn off.
    # After designing your beautiful Pixel Art PSA Cube, write your codes and connect your circuit to bring your project to life. 
    # Share it with your friends and family and show them why the Global Goals matter and what they can do to help make the world a better place!

## Parts of the Micro:bit Used
    
    # Pins (Digital Pins Control): Turning connected peripherals (like LEDs or motors) on or off using the micro:bit's digital pins.


## Programming Concepts
  
    # Looping (for loop): Repeating a set of actions a certain number of times.

    # Function: A block of code that performs a specific task or set of tasks.

    # Event Handling: Managing actions that occur continuously or repeatedly in the program.


## Programming Language
  # Python

## Coding Environment / Text Editor
  # Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

## Project Code / Program


def on_button_pressed_a():
    for index in range(50):
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(100)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    for index2 in range(20):
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(5000)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)
