"""## Introduction

Explore the world of streetlights with this micro:bit project! Utilize pins, LEDs, external LEDs and a light sensor to simulate a streetlight. 

The programming concepts involved include functions, loops, and conditional statements.


## Parts of the Micro:bit

1. **Pins:** Connectors used to interface with external components.
2. **LEDs (Light Emitting Diode):** Indicate different states of the streetlight.
3. **Light Sensor:** Detects ambient light levels.

## Programming Language
  Python


## Programming Concepts

- **Function:** A reusable block of code that performs a specific task. Functions will be used to control the streetlight states.
- **Loops:** Repeatedly execute a block of code.
- **Conditional Statements:** Make decisions in the code based on certain conditions.


## Coding Environment / Text Editor

   # [Microsoft MakeCode Editor](https://makecode.microbit.org/#editor)"""



# Project Code / Program ...

def on_forever():  # Define a function called on_forever
   
    if input.light_level() < 10:  # Check the light level
      
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)    # Show a pattern on the LED matrix when light level is less than 10
        
      
        pins.digital_write_pin(DigitalPin.P0, 1)   # Turn on pins P0
        pins.digital_write_pin(DigitalPin.P1, 1)   # Turn on pins  P1
    else:
       
        basic.clear_screen()  # If light level is not less than 10, clear the LED matrix
        
       
        pins.digital_write_pin(DigitalPin.P0, 0)  # Turn off pins P0 
        pins.digital_write_pin(DigitalPin.P1, 0)   # Turn off pins P1


basic.forever(on_forever) # Run the on_forever function repeatedly
