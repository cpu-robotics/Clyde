#!/usr/bin/env python
"""motor_control.py: Motor control via a Sabertooth 2x25 motor controller """

__author__      = "Nick Vazquez"
__copyright__   = "Copyright 2020, Davenport Central Robotics Teams"

# Import all Necessary Classes
import serial
import math
import functions

# Used for the verification of the baud rate by the motor controller
rateVerify = '170'

# Open a serial terminal with the port 'dev/tty0'
drive = serial.Serial(port='/dev/tty0')

# Print the name of the port that was connected to for verification
print(drive.name)

# Used by the Sabertooth motor controller to autodetect the Baud Rate used by the transmitting device
drive.write(rateVerify)

functions.trackDrive(130, 127, 'forward', 127)
