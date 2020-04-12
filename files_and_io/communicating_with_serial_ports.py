"""
This script shows how to read and write data over a serial port,
this is often used to interact with hardware (i.e robot or sensor)

The best way to do this is using pySerial package
"""
import serial
# Device name will vary
ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

"""
The device name will vary - once open you can use
read(), readline() and write() as follows
"""
ser.write(b'G1 x50 y50\r\n')
resp = ser.readline()

# From this point serial communication should be straight forward
# All input / output for serial ports is binary. struct module can help with this
