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


def forward(speed):

    speed = int((127/100)*speed)
    ser.write(b'L')
    ser.write([speed])
    sleep(.00001)
    ser.write(b'R')
    ser.write([speed])





print(ser.name) 

s=0

#Irtest
while True:

    
    ser.write(b'I')
    data = str(ser.read(1).hex())
    print(data)
    sleep(.0001)

    if data == "00" and s == 0:
        s=1
        forward(25)

    if data != "00" and s == 1:
           s=0 
           forward(0)


#TOF test
##while True:
##
##    
##    data = vl53.range
##    print(data)
##    sleep(.0001)
##
##    if data > 650 and s == 0:
##        s=1 
##        forward(0)
##    if data < 650 and s == 1:
##        s=0
##        forward(25)

        
    

##while True:
##
##    ser.write(b'I')
##    ir = str(ser.read(1).hex())
##    tof = vl53.range
##
##    
##    if (tof > 650 or ir != "00") and s == 0:
##        s=1 
##        forward(0)
##    if (tof < 650 and ir == "00") and s == 1:
##        s=0
##        forward(25)
    





    
