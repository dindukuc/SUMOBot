import string
import io
import math as m
import time
import board
import busio
import adafruit_vl53l0x
import serial

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
    ser.write(b'H')
    data = int(ser.read(1).hex(), 16)

    Btns[0] =   (data & 0b00001000) >> 3
    Btns[1] =   (data & 0b00000010) >> 1
    Btns[2] =   (data & 0b00000001) 
    Btns[3] =   (data & 0b00000100) >> 2
    text.value = str(Btns[0]) + "/" + str(Btns[1]) + "/" + str(Btns[2]) + "/" + str(Btns[3])

    return Btns

def getIR():
    IR = [0, 0, 0, 0]
    ser.write(b'I')
    data = ser.read(1).hex()

    IR[0] =   (data & 0b00001000) >> 3
    IR[1] =   (data & 0b00000010) >> 1
    IR[2] =   (data & 0b00000001) 
    IR[3] =   (data & 0b00000100) >> 2
    text.value = str(IR[0]) + "/" + str(IR[1]) + "/" + str(IR[2]) + "/" + str(IR[3])


    return IR

def getVolt():
    ser.write(b'E')
    data = ser.read(1).hex()
    

def getMotor():
    ser.write(b'M')
    data = ser.read(2).hex()


    
    
def updateSensor():


    text1.value = "ToF sensor: " + str(vl53.range)
    text2.value = "Battery Voltage: ")


init = 0

app = App("Display Sensor", layout="auto")
text1 = Text(app, text="ToF sensor: " + str(vl53.range))
text2 = Text(app, text="Battery Voltage: ")

text1.repeat(500, updateSensor)

app.display()

