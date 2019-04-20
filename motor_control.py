#!/usr/bin/env python
"""motor_control.py: Motor control via a Sabertooth 2x25 motor controller """

__author__      = "Nick Vazquez"
__copyright__   = "Copyright 2020, Davenport Central Robotics Teams"

# Import all Necessary Classes
import serial
import math

# Open a serial terminal with the port 'dev/tty0'
drive = serial.Serial(port='/dev/tty0')

# Used by the Sabertooth motor controller to autodetect the Baud Rate used by the transmitting device
drive.write(170)

functions.trackDrive(130, 127, 'forward', 0)
