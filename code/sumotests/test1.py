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
ser = serial.Serial('/dev/ttyS0', 38400, timeout=1)


#name = input("Type your name: ")
#message = input("Write a message: ")
#print(name + ' said, "' + message + '"')
#def counter():
#    text.value = int(text.value) + 1


#print(vl53.range)



def updateSensor():
    text1.value = "ToF sensor: " + str(vl53.range)
    text2.value = "Battery Voltage" + str(ser.read(2))


init = 0

app = App("Display Sensor", layout="auto")
text1 = Text(app, text="ToF sensor: " + str(vl53.range))


text.repeat(500, updateSensor)

app.display()

