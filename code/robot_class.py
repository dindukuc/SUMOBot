import io
import math as m
from time import sleep
import board
import busio
import adafruit_vl53l0x
import serial
from serial import *


i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
ser = serial.Serial('/dev/ttyS0',
                    38400,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=1)  # open serial port

class robot:
    i2c = busio.I2C(board.SCL, board.SDA)
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    ser = serial.Serial('/dev/ttyS0', 38400, timeout=1)

    tof = 0

    mL = [0, 0] #direction, speed
    mR = [0, 0] #direction, speed

    ir = [0, 0, 0, 0] #top left, top right, bottom left, bottom right

    bttn = [0, 0, 0, 0] #front , right, left, back

    imu = 0 #don't know how this works yet

    sensorData = 0 #keeps data that we can parse through

    def tof(self):
        self.tof = vl53.range
		return self.tof

    def ir(self):
        ser.write(b'I')
        data = str(ser.read(1).hex())
        return data
    
    def buttons(self):
        ser.write(b'H')
        data = str(ser.read(1).hex())
        return data

    def getSensors(self):
        ser.write(b'A')#request bulk serial data
        self.sensorData = ser.read(10)#read serial data


    def moveFwd(self, speed=100): #robot move forward
         
        if speed != 100:
            speed = int((127/100)*speed)
            ser.write(b'L')
            ser.write([speed])
            sleep(.00001)
            ser.write(b'R')
            ser.write([speed])
        else: 
            ser.write(b'F')
            sleep(.00001)



    def moveBck(self, speed=100): #robot move back
        
        if speed != 100:
            speed = int(~((127/100)*speed)+1)
            ser.write(b'L')
            ser.write([speed])
            sleep(.00001)
            ser.write(b'R')
            ser.write([speed])
        else: 
            ser.write(b'B')
            sleep(.00001)


    def stop(self): #stop motors
        ser.write(b'S')

    def turn(self, direction, time, speed):
        speed1 = int((127/100)*speed)
        speed2 = int(~((127/100)*speed)+1)
        
        
        if direction == 'L':
            ser.write(b'L')
            ser.write([speed2]) #move the motors so the robot turns left 
            sleep(.00001)
            ser.write(b'R')
            ser.write([speed1])
            
            if time > 0:
                time.sleep(time)
                self.stop()

        else:
            ser.write(b'R')
            ser.write([speed2]) #move the motors so the robot turns right 
            sleep(.00001)
            ser.write(b'L')
            ser.write([speed1])
            
            if time > 0:
                time.sleep(time)
                self.stop()

