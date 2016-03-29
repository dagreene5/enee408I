#!/usr/bin/python

import serial, os

#port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1);
port = os.open("/dev/ttyACM0", os.O_RDWR);

#port.flush();
os.write(port, "gp\n");
#port.flush();
os.fsync(port);

ret = os.readline(port);
#while ret == "":
#	port.flush();
	#port.write("gp\n");
#	port.flush();
	#ret = port.readline();
	
print("ping returned: " + ret);
