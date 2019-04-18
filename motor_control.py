#!/usr/bin/env python
"""motor_control.py: Motor control via a Sabertooth 2x25 motor controller """

__author__      = "Nick Vazquez"
__copyright__   = "Copyright 2020, Davenport Central Robotics Teams"

# Import all Necessary Classes
import serial
import math

# Define the operating modes for the motor controller
forwardMode     = 8
leftMode        = 11
rightMode       = 10

# Open a serial terminal with the port 'dev/tty0'
drive = serial.Serial(port='/dev/tty0')

# Print the name of the port that was connected to for verification
print(drive.name)

# Used by the Sabertooth motor controller to autodetect the Baud Rate used by the transmitting device
drive.write(170)


"""
driveForward: Function for driving the vehicle forward

Uses parameters:
    address: Address for the specified motor controller
    speedByte: Byte with value between 0-127 for the speed of the motor (Will map from 1-100 at later date)
    direction: Value between 127 and -127 specifing what direction the vehicle should be headed - + = Left, - = Right
"""
def driveForward(address, speedByte, direction):

    """
    Forward Speed Packet
    """
    drive.write(address)
    # powerMode is used to communicate with the controller that a power command is being sent
    drive.write(forwardMode)
    # Send the byte containing the desired speed to the controller
    drive.write(speedByte)
    # Calculate and send the checksum for the controller, which is address + command + data)
    checksum = address + forwardMode + speedByte
    drive.write(checksum)

    """
    Direction Packet
    """
    drive.write(address)

    # Determine if the mode should be either leftMode or rightMode based on the value of 'direction'
    # If 'direction' is positive, activate leftMode, and vice versa to go right
    if direction > 0:
        drive.write(leftMode)

    else:
        drive.write(rightMode)

    drive.write(abs(direction))

    print('Success!')
