#SUMO bot search and destroy algorithm

import string
import io
import math as m
import time
import board
import busio
import adafruit_vl53l0x
import serial
from serial import *

from robot_class import robot

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
ser = serial.Serial('/dev/ttyS0',
                    38400,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=1)  # open serial port


range = 650  #set IR range threshold (mm)

SumoBot = robot()

#Parse data??

#Sweep ring


#def button(): 

#    SumoBot.getSensors()
        
#          if SumoBot.bttn[1]:
#            SumoBot.moveFwd()
            





def search():
    SumoBot.turn("R", 0, 25)


    while True: 
        
        if SumoBot.tof() < range:
            start = time.time()
            
            while True:
                if SumoBot.tof() > range:
                    diff = time.time() - start 
                    SumoBot.turn("L",(diff/2), 25)
                    SumoBot.moveFwd(50)
                    
                    while SumoBot.tof() < range:
                        
                        if SumoBot.ir() != "00": 
                            SumoBot.stop()
                            SumoBot.moveBck(25)
                            time.sleep(.75)
                            SumoBot.turn("L", .5, 25)
                            break
                        
                        time.wait(.001)
                    break    
            break
    
    SumoBot.stop()            



while True:
    search()
    time.sleep(1) 










