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





def updateSensor():
    text1.value = "ToF sensor: " + str(vl53.range)
    text2.value = "Battery Voltage: " + str(ser.read(1))


init = 0

app = App("Display Sensor", layout="auto")
text1 = Text(app, text="ToF sensor: " + str(vl53.range))
text2 = Text(app, text="Battery Voltage: " + str(ser.read(1)))

text.repeat(500, updateSensor)

app.display()

