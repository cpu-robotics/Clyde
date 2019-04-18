
# drive = motor_control.drive

"""
driveForward: Function for driving the vehicle forward

Uses parameters:
    address:    Address for the specified motor controller
    speedByte:  Byte with value between 0-127 for the speed of the motor (Will map from 1-100 at later date)
    direction:  Either 'forward' or 'backward', specifing wither to drive forward or backward
    heading:    Value between 127 and -127 specifing what direction the vehicle should be headed - + = Left, - = Right
"""
def driveForward(address, speedByte, direction, heading):

    """
    Direction Packet
    """
    drive.write(address)

    # Determine wether to set the controller to forward or backward control mode
    if direction == 'forward':
        driveMode = forwardMode
    elif direction == 'backward':
        driveMode = backwardMode
    # If the direction was not forward or backward, throw an error
    else:
        raise ValueError('Direction was not forward or backward')

    # Send the driveMode to the controller
    drive.write(driveMode)
    # Send the byte containing the desired speed to the controller
    drive.write(speedByte)
    # Calculate and send the checksum for the controller, which is address + command + data)
    checksumDirection = address + driveMode + speedByte
    drive.write(checksumDirection)

    """
    Heading Packet
    """
    drive.write(address)

    # Determine if the mode should be either leftMode or rightMode based on the value of 'direction'
    # If 'direction' is positive, activate leftMode, and vice versa to go right
    if heading > 0:
        turnMode = leftMode
    else:
        turnMode = rightMode

    drive.write(turnMode)

    drive.write(abs(heading))

    checksumHeading = address + turnMode + abs(heading)

    drive.write(checksumHeading)

    print('Success!')
