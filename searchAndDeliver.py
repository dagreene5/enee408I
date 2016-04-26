#!/usr/bin/python
import struct
import sys
import serial
import time
from pixy import *
from ctypes import *

port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1);   # communication with arduino
file = open( "/dev/input/mice", "rb");                              # for optical input

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
    setRight(60);
    setLeft(70);

def travelBackward():
    moveBackward()
    setRight(60)
    setLeft(70)

def travelClockwise():
    rotateClockwise()
    setLeft(40)
    setRight(50)

def travelCounterClockwise():
    rotateCounterClockwise()
    setLeft(40)
    setRight(50)

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
global state_searching
global state_delivering
global min_cone_distance
global min_obstacle_distance
global lastDepositDirection

signature_cone = 1
num_cone_signatures = 2
signature_collection_box = 3
low_x_bound = 115
high_x_bound = 185
state_searching = 1
state_delivering = 2
#min_cone_distance = 10
min_cone_distance = 11
min_obstacle_distance = 30
lastDepositDirection = -1

global state
state = state_searching

def find_signature(blocks, count, signature):
    if (count > 0):
        for index in range (0, count):
            if (blocks[index].signature == signature):
                return (True, blocks[index].x, blocks[index].y)
    return (False,)

def dest_is_straight(x, y):
    global low_x_bound
    global high_x_bound
    return low_x_bound <= x <= high_x_bound

def dest_is_left(x, y):
    global low_x_bound
    return low_x_bound >= x

def dest_is_right(x, y):
    global high_x_bound
    return high_x_bound <= x

def carrying_cone():
    global min_cone_distance
    centerDistance = getPingCenter()
    print("center distance: " + str(centerDistance))
    return centerDistance <= min_cone_distance and centerDistance != 0

def obstacle_present(distance):
    global min_obstacle_distance
    return distance <= min_obstacle_distance and distance != 0

def is_blocked():
    leftDistance = getPingLeft()
    rightDistance = getPingRight()
    return False#(obstacle_present(leftDistance) and obstacle_present(rightDistance))

def grabCone():
    closeArms()
    #time.sleep(1)
    #stopArms()

def releaseCone():
    openArms()
    #time.sleep(1)
    #stopArms()

def dropOffConeManuever():
    global signature_cone
    halt()
    releaseCone()
    time.sleep(1)
    travelBackward()
    time.sleep(2)
    halt()
    travelClockwise()
    time.sleep(3)
    halt()
    if (signature_cone == 1):
        signature_cone = 2
    else:
        signature_cone = 1



def blind_search(carryingCone):
    leftDistance = getPingLeft()
    rightDistance = getPingRight()
    print("left distance: " + str(leftDistance))
    print("right distance: " + str(rightDistance))
    if (obstacle_present(leftDistance)):
        if (obstacle_present(rightDistance)):
            # fully blocked. Move in most available direction
            if (leftDistance < (rightDistance + 2)):
                # left obstacle is closer. Turn right
                print("object left and right, going right")
                travelClockwise()
            else:
                travelCounterClockwise()
                print("object left and right, going left")
        else:
            # just an obstacle left
            travelClockwise()
            print("object left, nothing right. Going right")
    elif (obstacle_present(rightDistance)):
        # just an obstacle right
        travelCounterClockwise()
        print("object right, nothing left. Going left")
    else:
        # no obstacles. Sprint if we don't have the cone, otherwise move more carefully
        print("no obstacles")
        if (carryingCone):
            travelForward()
        else:
            travelForwardFast()

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

    count = pixy_get_blocks(100, blocks)
    #leftDistance = getPingLeft()
    #centerDistance = getPingCenter()
    #rightDistance = getPingRight()
    cone_info = find_signature(blocks, count, signature_cone)
    #print("left distance: " + str(leftDistance))
    #print("right distance: " + str(rightDistance))
    #print("center distance: " + str(centerDistance))
    #print("pixy count: " + str(count))
    #print("cone info: " + str(cone_info[0]))



    if (state == state_searching):

        print("Searching for cone")
        
        if (cone_info[0]):           # cone in field of view
            cone_x = cone_info[1]
            cone_y = cone_info[2]
            print("Found cone")

            if (dest_is_straight(cone_x, cone_y)):

                # cone is in front of us. If we are carrying it, change state
                if (carrying_cone()):
                    state = state_delivering

                    halt()
                    grabCone()

                    if (lastDepositDirection == 1): # deposit was last left
                        travelCounterClockwise()
                    elif (lastDepositDirection == 2):
                        travelForward()
                    elif (lastDepositDirection == 3):
                        travelClockwise()
                    print("Transitioning to delivering")

                else:
                    travelForward()   # move to cone
                    print("Moving forward to cone")
                
            elif (dest_is_left(cone_x, cone_y)):
                # cone is to the left of us
                # an obstacle to the left of us is likely just the cone
                # just turn that way
                travelCounterClockwise()
                print("Moving left to cone. X: " + str(cone_x))
            else:
                # cone must be to the right. turn that way
                travelClockwise()
                print("Moving right to cone. X: " + str(cone_x))

        else:                   # cone not in field of view
            # blind search for now. Work in acceleromoter, do a 360 degree turn searching and then move to open space
            blind_search(False)
            print("Blind search")

    elif (state == state_delivering):

        print("Searching for delivery area")
        if (cone_info[0]): 


            # This mostly a backup incase we missed with the arms.. might take this out
            if (not (carrying_cone())):
                # cone is too far away. Search for it again
                print("Going back to searching")
                
                halt()
                releaseCone()

                state = state_searching
            else:
                # we are safely carrying the cone. Start looking for the collection area
                collection_info = find_signature(blocks, count, signature_collection_box)

                if (collection_info[0]):
                    # colletion area is visible and we are carrying the cone. Move to it
                    collection_x = collection_info[1]
                    collection_y = collection_info[2]

                    if (dest_is_straight(collection_x, collection_y)):
                        lastDepositDirection = 2
                        # dropoff area is straight ahead. Move towards it until both pings read an obstacle
                        if is_blocked():
                            halt()
                            print("reached destination. Releasing cone")
                            dropOffConeManuever()
                            state = state_searching

                                # we got it there! 
                                # Use the accelerometer to turn around 180 degrees and start searching again
                        else:

                            # revisit this case... maybe move towards where we detect an obstacle since it's
                            # probably the wall behind the collection area
                            moveForward()
                    elif (dest_is_left(collection_x, collection_y)):
                        lastDepositDirection = 1
                        travelCounterClockwise()
                    else:
                        lastDepositDirection = 3
                        travelClockwise()

                else:
                    lastDepositDirection = -1
                    # we do not see the collection area. For now do what we do when we don't see a cone
                    blind_search(True)

        else:
            # Something went wrong.. cone is not in field of view
            state = state_searching

file.close();
