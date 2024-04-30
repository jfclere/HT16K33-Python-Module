# HT16K33-Python-Module
Python 3.x module to use with a HT16K33 LED driver with keyscan IC. Testing done using an 
HT16K33 breakout board, 8x8 LED matrix, 4x3 row keypad and a 4 digit seven segment display all
from Adafruit.

This requires the smbus module for the i2c connection.

For connections to the HT16K33 from the Pi are as follows
- Pi SCL to HT16K33 SCL
- Pi SDA to HT16K33 SDA
- Pi 3.3V to HT16K33 Vdd
- Pi Gnd to HT16K33 Gnd

For connections from the HT16K33 to either a LED Matrix, 7 segment display and keypad
refer to the HT16K33 data sheets. Note if you are using a keypad with either an LED Matrix or
7 segment display don't forget the resistors between A3/K1-A15/K13 and the keypad, I used 20kOhm
and the diodes between COM1/KS0-COM3/KS2.

i2c address I used with A0-A2 floating was 0x70, this can be set to between 0x70 and 0x77.

Included is an example file which show the use of all the different functions 

Current functions include:

Common functions
- set_system_oscillator(state = 'ON')
- display_status(state = 'ON', blinkRate = 0)
- set_brightness(level = 15)
- set_interrupt(interrupt = False, active = 'HIGH')
- read_keyscan()

LED Matrix functions
- intialization: ledMatrix = HT16K33_LED_MATRIX(i2cAddress, i2cBus = 1, size = [8, 8], adafruit = False)
- fill_matrix(value = 1)
- invert_matrix()
- rotate_matrix(numTurns = 1)
- show_matrix()

4 Digit 7 Segment functions
- write_numbers(value, colonOn = False)
- set_justification(justification = "RIGHT")

November 5, 2020 Update
- added functionality to handle Adafruit 8x8 matrix backpacks

April 29, 2024 Update
- added i2c bus option
- added __setitem__ and rotate_matrix functs for LED matrix

Notes:
The HT16K33 data sheet is useful especially with connection diagrams etc






