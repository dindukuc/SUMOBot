import serial
ser = serial.Serial('/dev/ttyS0', 38400, timeout=1)  # open serial port
print(ser.name)         # check which port was really used

#ser.write(b'F')
#ser.write([13])     # write a string
#print(ser.read(2).hex())

def forward(speed):
    
    speed = int((128/100)*speed)
    ser.write(b'L')
    ser.write([speed])
    ser.write(b'R')
    ser.write([speed])

def backward(speed):
    
    speed = -int((128/100)*speed)
    ser.write(b'L')
    ser.write([speed])
    ser.write(b'R')
    ser.write([speed])
def stop():
    
    ser.write(b'L')
    ser.write([0])
    ser.write(b'R')
    ser.write([0])
    
    

ser.close()             # close port
