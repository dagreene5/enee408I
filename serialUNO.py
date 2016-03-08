#!/usr/bin/python
import serial
port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=3.0);

while 1:
	port.write("gl\n");
	port.flush();
	line = port.readline();
	print line
