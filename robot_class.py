import io
import math as m
import time
import board
import busio
import adafruit_vl53l0x
import serial



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
        return vl53.range

    def getSensors(self):
        ser.write(b'A')#request bulk serial data
        self.sensorData = ser.read(10)#read serial data


    def moveFwd(self, speed=100): #robot move forward
        ser.write(b'F')
        ser.write(int((127/100)*speed))

    def moveBck(self, speed=100): #robot move back
        ser.write(b'B')
        ser.write(int(128 + (127 / 100) * speed))


    def stop(self): #stop motors
        ser.write(b'S')

    def turn(self, direction = 'L', time):
        if direction == 'L':
            ser.write(b'L')
            ser.write(int(127)) #move the motors so the robot turns left 
            ser.write(b'R')
            ser.write(int(255))
            
            if time > 0:
                time.sleep(time)
                self.stop()

        else:
            ser.write(b'R')
            ser.write(int(127)) #move the motors so the robot turns right 
            ser.write(b'L')
            ser.write(int(255))
            
            if time > 0:
                time.sleep(time)
                self.stop()

