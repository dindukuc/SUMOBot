import string
import io
import math as m
import time
import board
import busio
import adafruit_vl53l0x
import serial
from serial import *
from guizero import App, Text

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
ser = serial.Serial('/dev/ttyS0',
                    38400,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=1) # open serial port



def getBtns():
    Btns = [0, 0, 0, 0]
    try:
        ser.write(b'H')
        data = ser.read(1)[0]

        Btns[0] =   (data & 0b00001000) >> 3
        Btns[1] =   (data & 0b00000010) >> 1
        Btns[2] =   (data & 0b00000001) 
        Btns[3] =   (data & 0b00000100) >> 2
        bttn.value = "Button sensors: " + str(Btns[0]) + "/" + str(Btns[1]) + "/" + str(Btns[2]) + "/" + str(Btns[3])
    except:
        pass
    #return Btns

def getIR():
    
    IR = [0, 0, 0, 0]
    ser.write(b'I')
    try:
        data = ser.read(1)[0]

        IR[0] =   (data & 0b00001000) >> 3
        IR[1] =   (data & 0b00000010) >> 1
        IR[2] =   (data & 0b00000001) 
        IR[3] =   (data & 0b00000100) >> 2
        ir.value = "IR sensors: " + str(IR[0]) + "/" + str(IR[1]) + "/" + str(IR[2]) + "/" + str(IR[3])
    except:
        pass        

        #return IR

def getVolt():
    ser.write(b'E')
    data = ser.read(1).hex()
    batt.value = "Battery Voltage: " + str(data)

def getMotor():
    ser.write(b'M')
    data = ser.read(2).hex()
    mtr.value = "Motor Speed: " + str(data)
    #ml = data[0] 
    #mr = 
    #speedL = int(data1,16)* (100/127)
    #speedR = int(data2,16)* (100/127)
	
	   
    
def updateTof():
	tof.value = "ToF sensor: " + str(vl53.range)
    


init = "0"

app = App("Display Sensor", layout="auto")

batt = Text(app, text="Battery Voltage: " + init)
tof = Text(app, text="ToF sensor: " + str(vl53.range))
ir = Text(app, text="IR sensors: " + init)
bttn = Text(app, text="Button sensors: " + init)
mtr = Text(app, text="Motor Speed: " + init)


tof.repeat(100, updateTof)
ir.repeat(50, getIR)
bttn.repeat(50, getBtns)
batt.repeat(1000, getVolt)
mtr.repeat(100, getMotor)

app.display()

