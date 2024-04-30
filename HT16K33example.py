#!/usr/bin/env python3
"""HT16K33example, example file for use with the HT16K33 python module.

created September 18, 2020
modified September 18, 2020
modified April 29, 2024 - added i2c bus option"""

"""
Copyright 2020 Owain Martin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time, sys, smbus
from HT16K33 import HT16K33, HT16K33_LED_MATRIX, HT16K33_7_SEGMENT

mode = 0

if mode == 0:

    ledMatrix = HT16K33_LED_MATRIX(0x70, 1, size = [8,8], adafruit = True)
    ledMatrix.fill_matrix(1)
    ledMatrix.show_matrix()
    time.sleep(2)
    ledMatrix.set_brightness(4)
    ledMatrix.display_status('ON', 1) # turn blinking on at 1Hz
    time.sleep(4)
    ledMatrix.display_status('ON', 0) # turn blinking off

    ledMatrix.matrix = [0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 1, 1, 0, 0, 1, 1, 0,
                        0, 1, 1, 0, 0, 1, 1, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 1, 0, 0, 0, 0, 1, 0,
                        0, 0, 1, 1, 1, 1, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0]
    ledMatrix.show_matrix()    
    time.sleep(2)
    ledMatrix.invert_matrix()
    ledMatrix.show_matrix()
    time.sleep(2)
    ledMatrix.invert_matrix()
    ledMatrix.show_matrix()
    time.sleep(2)

    for i in range(4):        
        ledMatrix.rotate_matrix(1)
        ledMatrix.show_matrix()
        time.sleep(2)

    ledMatrix.fill_matrix(0)
    ledMatrix[0] = 1
    ledMatrix[4] = 1
    ledMatrix.show_matrix()
    time.sleep(2)
    ledMatrix[8:16] = [1]*8
    ledMatrix[18] = 1
    ledMatrix[26] = 1
    ledMatrix[34:36] = [1]*2
    ledMatrix.show_matrix()
    time.sleep(2)
    

    """#Keyscan demo
    ledMatrix.set_interrupt(True, 'HIGH')
    startTime = time.time()
    loopLength = 10

    while (time.time()-startTime)<loopLength:
        print(ledMatrix.read_keyscan())       
        time.sleep(0.2)"""

    #Turn HT16K33 off
    ledMatrix.set_interrupt(False, 'HIGH')
    ledMatrix.display_status('OFF')
    ledMatrix.set_system_oscillator('OFF')

elif mode == 1:

    sevenSegment = HT16K33_7_SEGMENT(0x70, 1)
    sevenSegment.set_brightness(7)
    sevenSegment.set_justification("LEFT")    
    sevenSegment.write_numbers(-256.7)
    time.sleep(2)
    sevenSegment.write_numbers(91.3)
    time.sleep(2)
    sevenSegment.write_numbers(17.96)
    time.sleep(2)
    sevenSegment.write_numbers(None) # clear display
    time.sleep(2)
    sevenSegment.write_numbers(-8.5)
    time.sleep(2)
    
    # turn colon on and off every 1 second
    for i in range(0,5):
        sevenSegment.write_numbers(1004)
        time.sleep(1)
        sevenSegment.write_numbers(1004, True)
        time.sleep(1)

    #Turn HT16K33 off
    sevenSegment.write_numbers(None)
    sevenSegment.display_status('OFF')
    sevenSegment.set_system_oscillator('OFF')
