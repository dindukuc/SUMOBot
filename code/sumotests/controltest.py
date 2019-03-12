from guizero import App, Text, PushButton
import serial
from serial import*
from time import sleep

ser = serial.Serial('/dev/ttyS0',
                    38400,
                    parity=PARITY_NONE,
                    stopbits=STOPBITS_ONE,
                    bytesize=EIGHTBITS,
                    timeout=1)  # open serial port
print(ser.name)         # check which port was really used

#ser.write(b'F')
#ser.write([13])     # write a string
#print(ser.read(2).hex())

def forward(speed):


    ##ser.write(b'F')
    speed = int((127/100)*speed)
    ser.write(b'L')
    ser.write([speed])
    sleep(.00001)
    ser.write(b'R')
    ser.write([speed])

def backward(speed):


    ser.write(b'B')
##    speed = int(128 + (127/100)*speed)
##    ser.write(b'L')
##    ser.write([speed])
##    ser.write(b'R')
##    ser.write([speed])

def stop():
    
    ser.write(b'S')
    
def test():
##    ser.write(b'V')
##    data = ser.read(1).hex()
    ser.write(b'E')
    data = ser.read(1).hex()
    text.value = int(data, 16)
    print(data)


    
    
    #time.sleep(.75)
    #text.value = ""

#def clear():
    #print("test")
    #text.value = ""
    #text.hide()
    #text.show()

app = App("Display Sensor", layout="auto")


button1 = PushButton(app, text="Forward", command=forward, args=[100])
button2 = PushButton(app, text="Stop", command=stop)
button3 = PushButton(app, text="Backward", command=backward, args=[100])
button4 = PushButton(app, text="V", command=test)
#button5 = PushButton(app, text="V", command=clear)
text = Text(app, text ="", visible=True)

#button4.after(3, clear)


app.display()






ser.close()             # close port
