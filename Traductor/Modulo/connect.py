import serial

try:
	conn = serial.Serial("COM1", 9600)
except Exception as e:
	raise
else:
	conn = serial.Serial("COM2", 9600)
else:
	conn = serial.Serial("COM4", 9600)
finally:
	conn = serial.Serial("COM5", 9600)
