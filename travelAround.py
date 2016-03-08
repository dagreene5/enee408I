#!/usr/bin/python
import struct



import serial
port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=.01);
file = open( "/dev/input/mice", "rb");

def setLeft(pwm):
    port.write("sl " + str(pwm) + "\n");
    port.flush();
    return;

def setRight(pwm):
    port.write("sr " + str(pwm) + "\n");
    port.flush();
    return;

def setBoth(pwm):
    port.write("sb " + str(pwm) + "\n");
    port.flush();
    return;

def incrementLeft(pwm):
    port.write("il " + str(pwm) + "\n");
    port.flush();
    return;

def incrementRight(pwm):
    port.write("ir " + str(pwm) + "\n");
    port.flush();
    return;

def halt():
    port.write("h\n");
    port.flush();
    return;

def rotateClockwise():
    port.write("smcw\n");
    port.flush();
    return;

def rotateCounterClockwise():
    port.write("smcc\n");
    port.flush();
    return;

def moveForward():
    port.write("smf\n");
    port.flush();
    return;

def moveBackward():
    port.write("smb\n");
    port.flush();
    return;

def getPing():
    port.flush();
    port.write("gp\n");
    port.flush();
    ret = port.readline();
    print("ping returned: " + ret);
    return int(ret.rstrip());

def getLeftPWM():
    port.write("gl\n");
    port.flush();
    return int(port.readline().rstrip());

def getRightPWM():
    port.write("gr\n");
    port.flush();
    return port.readline();

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

def getDx():
    buf = file.read(3);
    button = ord( buf[0] );
    x,y = struct.unpack( "bb", buf[1: ]);
    return x;


port.flush();
setBoth(50);
port.flush();

while (1):
    distance = getPing();
    print("distance: " + str(distance) + "\n");
    if (distance != 0 and distance < 20):
        print("distance is too small, rotating\n");
        halt();
        rotateClockwise();
        setBoth(50);
        while (distance < 20):
            distance = getPing();
        halt();
        moveForward();
        setBoth(50);
        
    else:
        print("moving forward\n");
        dx = getDx();
        incrementLeft(-dx);
        incrementRight(dx);

file.close();
