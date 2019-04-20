#!/usr/bin/env python
"""
human_control.py: Program for human control of the "Sabertooth 2x25" motor controller.
"""

import serial
import functions

drive = serial.Serial(port='/dev/tty0')

print(drive.name)

drive.write(170)

try:
    while True:
        address = input("What address are we controlling?: ")
        speed = input("What is the desired speed?: ")
        direction = input("What is the desired direction?: ")
        heading = input("What is the desired heading?: ")

        functions.trackDrive(address, speed, direction, heading)

except KeyboardInterrupt:
    print('Interrupted!')
