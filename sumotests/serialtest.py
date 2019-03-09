import serial
import time

ser = serial.Serial('/dev/ttyS0', 38400, timeout=1)  # open serial port
print(ser.name)         # check which port was really used

#ser.write(b'F')
#ser.write([13])     # write a string



while(True):
	print(ser.read(2).hex())
	time.sleep(.5)


ser.close()             # close port
