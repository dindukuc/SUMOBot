from serial import *
import serial
from time import sleep
import board
import busio
import adafruit_vl53l0x


i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
ser = serial.Serial('/dev/ttyS0',
                    38400,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=1)  # open serial port



ser.write(b'S')
