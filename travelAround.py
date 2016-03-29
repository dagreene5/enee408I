#!/usr/bin/python
import struct
import sys
sys.path.insert(0, '/PixyCode/build/libpixyusb_swig')
import pixy
import serial

port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1);   # communication with arduino
file = open( "/dev/input/mice", "rb");                              # for optical input

maxPwm = 60;
minPwm = -60;


def setLeft(pwm):
    port.write("sl " + str(pwm) + "e");
    return;

def setRight(pwm):
    port.write("sr " + str(pwm) + "e");
    return;

def setBoth(pwm):
    port.write("sb " + str(pwm) + "e");
    return;

def incrementLeft(pwm):
    port.write("il " + str(pwm) + "e");
    return;

def incrementRight(pwm):
    port.write("ir " + str(pwm) + "e");
    return;

def incrementLeftToMax(pwm):
    port.write("il " + str(pwm) + "e");
    leftPwm = getLeftPWM();
    if (leftPwm > maxPwm):
        setLeft(maxPwm);
    elif (leftPwm < minPwm):
        setLeft(minPwm);
    return;

def incrementRightToMax(pwm):
    port.write("ir " + str(pwm) + "e");
    rightPwm = getRightPWM();
    if (rightPwm > maxPwm):
        setRight(maxPwm);
    elif (rightPwm < minPwm):
        setRight(minPwm);
    return;

def halt():
    port.write("he");
    return;

def rotateClockwise():
    port.write("smcwe");
    return;

def rotateCounterClockwise():
    port.write("smcce");
    return;

def moveForward():
    port.write("smfe");
    return;

def moveBackward():
    port.write("smbe");
    return;

def getPingLeft():
    port.write("gple");
    ret = port.readline();
    return int(ret);

def getPingRight():
    port.write("gpre");
    ret = port.readline();
    return int(ret);

def getLeftPWM():
    port.write("gle");
    return int(port.readline().rstrip());

def getRightPWM():
    port.write("gre");
    return port.readline();

def getMouseEvent():
    buf = file.read(3);
    button = ord( buf[0] );
    # bLeft = button & 0x1;
    # bMiddle = ( button & 0x4 ) > 0;
    # bRight = ( button & 0x2 ) > 0;
    x,y = struct.unpack( "bb", buf[1:] );
    port.write("il " + str(-x) + "\nir " + str(x) + "e");
    port.flush();
    # print ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight,x,y));
    # return

def getDx():
    buf = file.read(3);
    button = ord( buf[0] );
    x,y = struct.unpack( "bb", buf[1: ]);
    return x;

def travelForward():
    moveForward();
    setRight(30);
    setLeft(40);

def objectDetected(distance):
    return distance != 0 and distance < 20;

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data;
        self.next_node = next_node;

    def get_data(self):
        return self.data;

    def get_next(self):
        return self.next_node;

    def set_next(self, new_next):
        self.next_node = new_next;

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head;
        self.tail = head;

    def enqueue(self, data):
        new_node = Node(data);
        self.tail.set_next(new_node);
        self.tail = self.tail.next_node;

    def size(self):
        current = self.head;
        count = 0;
        while current:
            count += 1;
            current = current.get_next();
        return count;

    def dequeue(self):
        temp = self.head;
        self.head = self.head.next_node;
        return temp;


port.flush();
#setBoth(50);
port.flush();

# stupid initialization: flush buffer
response = "";
while (response == ""):
    port.write("gple");
    port.flush();
    response = port.readline();

# Pixy init
pixy_init();

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]
blocks = BlockArray(100)
frame  = 0

signature_cone_low = 1
signature_cone_high = 1

def look_for_cone():
    count = pixy_get_blocks(100, blocks)

    if (count > 0):
        frame = frame + 1
        for index in range (0, count):
            if (signature_cone_low <= blocks[index].signature <= signature_cone_high):
                print("x: " + str(blocks[index].x) + "y: " + str(blocks[index].y));




while (1):

    distanceLeft = getPingLeft();
    distanceRight = getPingRight();

    if (objectDetected(distanceLeft) or
        objectDetected(distanceRight)):

        if (objectDetected(distanceLeft)):
            rotateCounterClockwise();
        elif (objectDetected(distanceRight)):        
            rotateClockwise();

        while (objectDetected(distanceLeft) or
            objectDetected(distanceRight)):

            distanceLeft = getPingLeft();
            distanceRight = getPingRight();
            
        halt();
        travelForward();
        
    else:
        travelForward();
        look_for_cone();
       

file.close();
