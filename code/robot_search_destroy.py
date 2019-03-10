#SUMO bot search and destroy algorithm

import string
import io
import math as m
import time
import board
import busio
import adafruit_vl53l0x
import serial

from robot_class import robot

range = 650  #set IR range threshold (mm)

SumoBot = robot()

#Parse data??

#Sweep ring


def button(): 

    SumoBot.getSensors()
        
        if SumoBot.bttn[1]:
            SumoBot.moveFwd()
            





def search():
    SumoBot.turn(R, 0)


    while True: 
        
        if SumoBot.tof() < range:
            start = time.time()
            
            while True:
                if SumoBot.tof() > range:
                    diff = time.time() - start 
                    SumoBot.turn(L,(diff/2))
                    SumoBot.moveFwd()
                    
                    while SumoBot.tof() < range:
                        time.wait(.001)
                    break    
            break
    
    SumoBot.stop()            





while True: 
    SumoBot.getSensors()


    if(): #IR line
          #
    










