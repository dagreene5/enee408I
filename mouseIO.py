#!/usr/bin/python
import struct



import serial
port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=3.0);
file = open( "/dev/input/mice", "rb");

def getMouseEvent():
    buf = file.read(3);
    button = ord( buf[0] );
    # bLeft = button & 0x1;
    # bMiddle = ( button & 0x4 ) > 0;
    # bRight = ( button & 0x2 ) > 0;
    x,y = struct.unpack( "bb", buf[1:] );
    port.write("il " + str(-x) + "\nir " + str(x) + "\n");
    port.flush();
    # print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight,x,y));
    # return

port.flush();
port.write("sl 50\nsr 50\n");

while (1):
    getMouseEvent();
file.close();
