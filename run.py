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

def backward(speed):

    speed = 256 - int((127/100)*speed)
    ser.write(b'L')
    ser.write([speed])
    sleep(.00001)
    ser.write(b'R')
    ser.write([speed])

def stop():
    
    ser.write(b'S')

def rot(speed, time, dir):

    speed1 = int((127/100)*speed)
    speed2 = 256 - int((127/100)*speed)
    
    if dir == "R":
        ser.write(b'L')
        ser.write([speed1])
        sleep(.00001)
        ser.write(b'R')
        ser.write([speed2])
    
    elif dir == "L":
        ser.write(b'R')
        ser.write([speed1])
        sleep(.00001)
        ser.write(b'L')
        ser.write([speed2])

    if time > 0:
        sleep(time)
        stop()

def evadeEdge(ir):
    if ir == "04" or ir == "08" or ir == "0c":
        stop()
        backward(50)
        sleep(.75)
        rot(50, .6, "R")
    elif ir == "01" or ir == "02" or ir == "03":
        stop()
        forward(50)
        sleep(.75)
        rot(50, .6, "L")

def defend(btn):
    if btn == "08":      #front
        forward(90)

    elif btn == "02":    #left
        rot(50, .5, "L")

    elif btn == "01":    #right
        rot(50, .5, "R")

    elif btn == "04":    #back
        backward(90)

# def superEvade(ir, btn):


s = "start"

while True:
    ser.write(b'I')
    ir = str(ser.read(1).hex())
    print(ir)
    ser.write(b'H')
    btn = str(ser.read(1).hex())
    tof = vl53.range
    sleep(.0001)
    

    #state 0 search
    #state 1 charge if spotted
    #state 2 stop charge
    #state 3 evade edge
    if s ==  "start":
        s = "search"

    elif s == "search":
        rot(25, 0, "L")

    elif s == "charge":
        #sleep(.1)
        forward(75)

    elif s == "defend":
        defend(btn)
        s = "search"

    # elif s == "superEvade":
    #     superEvade()

    elif s == "evadeEdge":
        print("evadeedge")
        evadeEdge(ir)
        s = "start"

    if tof < 550 and s == "search":
        s = "charge"

    elif tof > 500 and s =="charge":
        s = "search"
    
    #button

    # if ir != "00" and btn != "00":
    #     s = "superEvade"

    if btn == "03":
        stop()
        print("I died :(")
        break;
    if ir != "00":
        s = "evadeEdge"

    elif btn != "00":
        s = "defend"

    

    
