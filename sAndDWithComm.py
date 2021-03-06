#!/usr/bin/python
import struct
import sys
import serial
import time
import socket
from pixy import *
from ctypes import *

port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1);   # communication with arduino
#file = open( "/dev/input/mice", "rb");                              # for optical input


# TCP connection init
TCP_IP = '192.168.0.100'
TCP_PORT = 5005
BUFFER_SIZE = 1024

print("Connecting to server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("Connected")


maxPwm = 60;
minPwm = -60;

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pixy', [dirname(__file__)])
        except ImportError:
            import _pixy
            return _pixy
        if fp is not None:
            try:
                _mod = imp.load_module('_pixy', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pixy = swig_import_helper()
    del swig_import_helper
else:
    import _pixy
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class BlockArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BlockArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pixy.new_BlockArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pixy.delete_BlockArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pixy.BlockArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pixy.BlockArray___setitem__(self, *args)
    def cast(self): return _pixy.BlockArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pixy.BlockArray_frompointer
    if _newclass:frompointer = staticmethod(_pixy.BlockArray_frompointer)
BlockArray_swigregister = _pixy.BlockArray_swigregister
BlockArray_swigregister(BlockArray)

def BlockArray_frompointer(*args):
  return _pixy.BlockArray_frompointer(*args)
BlockArray_frompointer = _pixy.BlockArray_frompointer


def pixy_init():
  return _pixy.pixy_init()
pixy_init = _pixy.pixy_init

def pixy_get_blocks(*args):
  return _pixy.pixy_get_blocks(*args)
pixy_get_blocks = _pixy.pixy_get_blocks

def pixy_close():
  return _pixy.pixy_close()
pixy_close = _pixy.pixy_close
class Block(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Block, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Block, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _pixy.Block_type_set
    __swig_getmethods__["type"] = _pixy.Block_type_get
    if _newclass:type = _swig_property(_pixy.Block_type_get, _pixy.Block_type_set)
    __swig_setmethods__["signature"] = _pixy.Block_signature_set
    __swig_getmethods__["signature"] = _pixy.Block_signature_get
    if _newclass:signature = _swig_property(_pixy.Block_signature_get, _pixy.Block_signature_set)
    __swig_setmethods__["x"] = _pixy.Block_x_set
    __swig_getmethods__["x"] = _pixy.Block_x_get
    if _newclass:x = _swig_property(_pixy.Block_x_get, _pixy.Block_x_set)
    __swig_setmethods__["y"] = _pixy.Block_y_set
    __swig_getmethods__["y"] = _pixy.Block_y_get
    if _newclass:y = _swig_property(_pixy.Block_y_get, _pixy.Block_y_set)
    __swig_setmethods__["width"] = _pixy.Block_width_set
    __swig_getmethods__["width"] = _pixy.Block_width_get
    if _newclass:width = _swig_property(_pixy.Block_width_get, _pixy.Block_width_set)
    __swig_setmethods__["height"] = _pixy.Block_height_set
    __swig_getmethods__["height"] = _pixy.Block_height_get
    if _newclass:height = _swig_property(_pixy.Block_height_get, _pixy.Block_height_set)
    __swig_setmethods__["angle"] = _pixy.Block_angle_set
    __swig_getmethods__["angle"] = _pixy.Block_angle_get
    if _newclass:angle = _swig_property(_pixy.Block_angle_get, _pixy.Block_angle_set)
    def __init__(self): 
        this = _pixy.new_Block()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pixy.delete_Block
    __del__ = lambda self : None;
Block_swigregister = _pixy.Block_swigregister
Block_swigregister(Block)


#############################################
#               Arduino Conrols             #
#############################################

def openArms():
    port.write("av 250e");
    return;

def closeArms():
    port.write("av 3e");
    return;

def stopArms():
    port.write("av 0e");
    return;

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

def getPingCenter():
    port.write("gpce");
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

def travelForwardFast():
    moveForward();
    setRight(70);
    setLeft(80);

def travelForward():
    moveForward();
    setRight(75);
    setLeft(85);

def travelBackward():
    moveBackward()
    setRight(70)
    setLeft(80)

def travelClockwise():
    rotateClockwise()
    setLeft(50)
    setRight(60)

def travelCounterClockwise():
    rotateCounterClockwise()
    setLeft(50)
    setRight(60)

def objectDetected(distance):
    return distance != 0 and distance < 30;

def is_clear(distance):
    return distance == 0 or distance >= 30;

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


################################################################################
#                       PI UTILITY FUNCTIONS                                   #
################################################################################

global signature_cone
global num_cone_signatures
global signature_collection_box
global low_x_bound
global high_x_bound
global min_cone_distance
global min_obstacle_distance
global lastDepositDirection

# States...
global state_request_sig
global state_searching
global state_request_grab
global state_grabbing
global state_searching_for_delivery_area
global state_request_deliver
global state_delivering
global state_confirm_delivery

global blockedCount
global lastX
global lastY
global centerDistance
global cycleCount

cycleCount = 0
centerDistance = -1
lastX = -1
lastY = -1
blockedCount = 0

state_request_sig = 1
state_searching = 3
state_request_grab = 4
state_grabbing = 6
state_searching_for_delivery_area = 11
state_request_deliver = 7
state_delivering = 9
state_confirm_delivery = 10

global state
state = state_request_sig


signature_cone = 1
num_cone_signatures = 2
signature_collection_box = 3
low_x_bound = 115
high_x_bound = 185
min_cone_distance = 9
min_obstacle_distance = 30
lastDepositDirection = -1




def find_signature(blocks, count, signature):
    if (count > 0):
        for index in range (0, count):
            if (blocks[index].signature == signature or (not(blocks[index].signature == 3) and signature == 0)) :
                return (True, blocks[index].x, blocks[index].y, blocks[index].signature)
    return (False,)

def dest_is_straight(x, y):
    global low_x_bound
    global high_x_bound
    return 115 <= x <= 185

def dest_is_left(x, y):
    global low_x_bound
    return low_x_bound >= x

def dest_is_right(x, y):
    global high_x_bound
    return high_x_bound <= x

def carrying_cone():
    global min_cone_distance
    global centerDistance

    if (centerDistance == -1):
        centerDistance = getPingCenter()

    if (centerDistance <= min_cone_distance and centerDistance != 0):
        halt()
        time.sleep(.5)
        count = 0
        while (count <= 10):
            centerDistance = getPingCenter()
            time.sleep(.1)

            if (not(centerDistance <= min_cone_distance and centerDistance != 0)):
                travelForward()
                return False
            count = count + 1
        return True
            
    return False

def obstacle_present(distance):
    global min_obstacle_distance
    return distance <= min_obstacle_distance and distance != 0

def is_blocked(x, y):
    global leftDistance
    global rightDistance
    global blockedCount
    global centerDistance
    global lastX, lastY

    if (lastX == -1 or lastY == -1):
        return False
    print("X, Y: " + str(x) + ", " + str(y))
    if (abs(x - lastX) < 5 and abs(y - lastY) < 5):
        blockedCount = blockedCount + 1
        if (blockedCount == 3):
            blockedCount = 0
            centerDistance = -1
            return True

    return False

def grabCone():
    stopArms()
    time.sleep(1)
    closeArms()
    time.sleep(1)
    stopArms()

def releaseCone():
    stopArms()
    time.sleep(1)
    openArms()
    time.sleep(1)
    stopArms()

def dropOffConeManuever():
    global signature_cone
    halt()
    time.sleep(.5)
    travelBackward()
    time.sleep(1)
    halt()
    time.sleep(.5)
    releaseCone()
    time.sleep(2)
    travelBackward()
    time.sleep(.5)
    halt()
    time.sleep(.5)
    travelClockwise()
    time.sleep(2.5)
    halt()
    time.sleep(.5)



def blind_search(carryingCone):
    global centerDistance
    #leftDistance = getPingLeft()
    #rightDistance = getPingRight()
    #print("left distance: " + str(leftDistance))
    #print("right distance: " + str(rightDistance))
    #if (obstacle_present(leftDistance)):
    #    if (obstacle_present(rightDistance)):
            # fully blocked. Move in most available direction
    #        if (leftDistance < (rightDistance + 2)):
                # left obstacle is closer. Turn right
    #            print("object left and right, going right")
    #            travelClockwise()
    #        else:
    #            travelCounterClockwise()
    #            print("object left and right, going left")
    #    else:
            # just an obstacle left
    #        travelClockwise()
    #        print("object left, nothing right. Going right")
    #elif (obstacle_present(rightDistance)):
        # just an obstacle right
    #    travelCounterClockwise()
    #    print("object right, nothing left. Going left")
    #else:
        # no obstacles. Sprint if we don't have the cone, otherwise move more carefully
    if (carryingCone):
        travelClockwise()
    else:
        if (centerDistance == -1):
            centerDistance = getPingCenter()
        if (centerDistance == 0 or centerDistance > 60):
            travelForward()
        else:
            travelClockwise()

#########################################################################################
#                                   BEGIN CODE                                          #
#########################################################################################


port.flush();
#setBoth(50);
port.flush();

# for buffer to flush so we can communicate with the arduino
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


# Initialize arm position
releaseCone()



while (1):

    global state
    global state_request_sig
    global state_searching
    global state_request_grab
    global state_grabbing
    global state_searching_for_delivery_area
    global state_request_deliver
    global state_delivering
    global state_confirm_delivery
    global centerDistance
    global cycleCount
    global lastX
    global lastY

    cycleCount = (cycleCount + 1) % 5

    if (cycleCount == 4):
        centerDistance = -1

    if (state == state_request_sig):
        halt()
        s.send("r")
        sig = ""
        print("Requesting what signature to look for...")
        while (sig == ""):
            sig = s.recv(BUFFER_SIZE)
        print("Received: " + sig)

        if (sig == "1"):
            signature_cone = 1
        elif (sig == "2"):
            signature_cone = 2
        else:
            signature_cone = 0

        state = state_searching

    elif (state == state_searching):
        count = pixy_get_blocks(100, blocks)
        cone_info = find_signature(blocks, count, signature_cone)
        
        if (cone_info[0]):           # cone in field of view
            signature_cone = cone_info[3] # if it was 0, now set to 1 or 2
            state = state_request_grab
        else:                   # cone not in field of view
            # blind search for now. Work in acceleromoter, do a 360 degree turn searching and then move to open space
            blind_search(False)

    elif (state == state_request_grab):
        halt()
        if (signature_cone == 1):
            print("Requesting to grab 1")
            s.send("g1")
        else:
            print("Requesting to grab 2")
            s.send("g2")
        response = ""
        while (response == ""):
            response = s.recv(BUFFER_SIZE)

        print("Received response: " + response)
        if (response == "c"):
            state = state_grabbing
        else:
            # Flip what we're looking for...
            if (signature_cone == 1):
                signature_cone = 2
            else:
                signature_cone = 1
            state = state_searching

    elif (state == state_grabbing):
        count = pixy_get_blocks(100, blocks)
        cone_info = find_signature(blocks, count, signature_cone) 

        if (cone_info[0]):

            cone_x = cone_info[1]
            cone_y = cone_info[2]
            if (dest_is_straight(cone_x, cone_y)):

                # cone is in front of us. If we are carrying it, change state
                if (carrying_cone()):

                    halt()
                    print("Grabbing cone")
                    grabCone()
                    print("Got cone. Searching for delivery area")
                        
                    state = state_searching_for_delivery_area
                    #else:
                     #   releaseCone() # try again to grab...
                else:
                    travelForward()   # move to cone
                
            elif (dest_is_left(cone_x, cone_y)):
                # cone is to the left of us
                # an obstacle to the left of us is likely just the cone
                # just turn that way
                travelCounterClockwise()
            else:
                # cone must be to the right. turn that way
                travelClockwise()
        else:
            # We lost it, but blind search for the one we were assigned
            blind_search(False)

    elif (state == state_searching_for_delivery_area):
        count = pixy_get_blocks(100, blocks)
        collection_info = find_signature(blocks, count, signature_collection_box)

        if (collection_info[0]):
            state = state_request_deliver
        else:
            print("Do not see collection area")
            # we do not see the collection area. For now do what we do when we don't see a cone
            blind_search(True)
    elif(state == state_request_deliver):
        halt()
        if (signature_cone == 1):
            print("Requesting to deliver 1")
            s.send("d1")
        else:
            print("Requesting to deliver 2")
            s.send("d2")
        response = ""
        while (response == ""):
            response = s.recv(BUFFER_SIZE)
        print("Received response: " + response)
        if (response == "c"):
            state = state_delivering
        else:
            dropOffConeManuever()
            if (signature_cone == 1):
                signature_cone = 2
            else:
                signature_cone = 1
            state = state_searching

    elif(state == state_delivering):
        # colletion area is visible and we are carrying the cone. Move to it
        count = pixy_get_blocks(100, blocks)
        collection_info = find_signature(blocks, count, signature_collection_box)

        if (collection_info[0]):
            collection_x = collection_info[1]
            collection_y = collection_info[2]

            if (dest_is_straight(collection_x, collection_y)):
                # dropoff area is straight ahead. Move towards it until both pings read an obstacle
                if is_blocked(collection_x, collection_y):
                    halt()
                    dropOffConeManuever()
                    state = state_confirm_delivery

                        # we got it there! 
                        # Use the accelerometer to turn around 180 degrees and start searching again
                else:

                    # revisit this case... maybe move towards where we detect an obstacle since it's
                    # probably the wall behind the collection area
                    travelForward()
                    time.sleep(1)
                    lastX = collection_x
                    lastY = collection_y
            elif (dest_is_left(collection_x, collection_y)):
                travelCounterClockwise()
            else:
                travelClockwise()
        else:
            print("no longer see collection box. blind searching")
            blind_search(True)
    elif (state == state_confirm_delivery):
        halt()
        print("Signature_cone: " + str(signature_cone))
        if (signature_cone == 1):
            print("Sending signal confirmed delivery 1")
            s.send("cd1")
        elif (signature_cone == 2):
            print("Sending signal confirmed delivery 2")
            s.send("cd2")
        time.sleep(1)
        state = state_request_sig

       

file.close();
