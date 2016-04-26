#!/usr/bin/python
import struct
import serial

port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1);   # communication with arduino
             # for optical input


def halt():
    port.write("he");
    return;

def turnOffServo():
    port.write("av 0e");
    return;

def getPingLeft():
    port.write("gple");
    ret = port.readline();
    print("ping returned: " + ret);
    return int(ret);

response = "";
while (response == ""):
    port.write("gple");
    port.flush();
    response = port.readline();

halt();
turnOffServo();
file.close();
