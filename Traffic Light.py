"""## Introduction

Experience the world of traffic lights by creating your own simulation  using LEDs connected to specific pins on the micro:bit!

This project involves the use of pins, LEDs, and programming concepts like functions. 
Please note that the timer for light changes in this simulation does not adhere to real-world traffic light standards.


## Parts of the Micro:bit

1. **Pins:** Connectors used to interface with external components.
2. **LEDs (Light Emitting Diode):** Indicate different states of the traffic light.



## Programming Concepts

 **Function:** A reusable block of code that performs a specific task. 


## Programming Language

  Python


## Coding Environment / Text Editor
     ##[Microsoft MakeCode Editor](https://makecode.microbit.org/#editor)


## Feel free to comment or contribute"""




# Project Code / Program ...

def on_forever(): # Define a function called on_forever
    pins.digital_write_pin(DigitalPin.P0, 1)   # Turn on the red light (P0)
    basic.pause(5000)  # Pause for 5 seconds
    basic.pause(5000)    # Pause for an additional 5 seconds
    pins.digital_write_pin(DigitalPin.P0, 0)  # Turn off the red light (P0)

    pins.digital_write_pin(DigitalPin.P1, 1)   # Turn on the amber light (P1)
    basic.pause(5000)
    basic.pause(5000)
    pins.digital_write_pin(DigitalPin.P1, 0) # Turn off the amber light (P1)

  
    pins.digital_write_pin(DigitalPin.P2, 1)  # Turn on the green light (P2)
    basic.pause(5000)
    basic.pause(5000)
    pins.digital_write_pin(DigitalPin.P2, 0) # Turn off the green light (P2)

basic.forever(on_forever) # Run the on_forever function repeatedly
