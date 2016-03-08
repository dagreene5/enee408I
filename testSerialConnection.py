#!/usr/bin/python

import serial
port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=.01);


port.write("gp\n");
port.flush();
ret = port.readline();
print("ping returned: " + ret);