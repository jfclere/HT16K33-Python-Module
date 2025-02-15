#!/usr/bin/env python3
"""example that display time using the HT16K33 python module


"""
"""
Copyright 2024 Jean-Frederic Clere

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

import time, sys, smbus, datetime, signal, sys
from HT16K33 import HT16K33, HT16K33_7_SEGMENT

class HT16K33time:

  def __init__(self):

    self.sevenSegment = HT16K33_7_SEGMENT(0x70, 1)
    self.sevenSegment.set_brightness(7)
    self.sevenSegment.set_justification("LEFT")
    return

  def off(self):
    #Turn HT16K33 off
    self.sevenSegment.write_numbers(None)
    self.sevenSegment.display_status('OFF')
    self.sevenSegment.set_system_oscillator('OFF')
    return

  def display(self, val, on):

    self.sevenSegment.write_numbers(val, on)
    return

  def hourminu(self):
    now = datetime.datetime.now()
    print(now.time())
    hour = now.strftime('%H')
    minu = now.strftime('%M')
    print(hour)
    print(minu)
    val = int(hour)
    val = val * 100
    val = val + int(minu)
    return val

  def signal_handler(self, sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
    self.off()

if __name__ == "__main__":

    myout = HT16K33time()

    signal.signal(signal.SIGINT, myout.signal_handler)
    print('Press Ctrl+C To stop')

    i = 0
    while True:
      val = myout.hourminu()
      if i % 2 == 0:
        myout.display(val, True)
      else:
        myout.display(val, False)
      time.sleep(1)
      i = i + 1
    myout.off()
