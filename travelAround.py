#!/usr/bin/python
import struct
import sys
import serial
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


#########################################################################################
#                                   BEGIN CODE                                          #
#########################################################################################


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

signature_cone_low = 1
signature_cone_high = 1
signature_collection_box = 2
low_x_bound = 135
high_x_bound = 165
looking_for_cone = 1
delivering_cone = 2
minConeCarryDistance = 10

state = looking_for_cone

def move_to_open_space():
    distanceLeft = getPingLeft();
    distanceRight = getPingRight();

    if (distanceLeft == 0):
        if (distanceRight == 0):    # open space
            travelForward()
        else:                       # left is clear, rotate that direction
            rotateCounterClockwise()
    elif (distanceRight == 0):      # right is clear, rotate that direction
        rotateClockwise()
    else:                           # go in the more open direction
        if (distanceRight < distanceLeft):  # more immediate obstacle right, go left
            rotateCounterClockwise();
        else:
            rotateClockwise();

def move_towards_coordinate(x, y):
    if (low_x_bound <= x <= high_x_bound):
        travelForward();
    elif (low_x_bound >= x):
        rotateCounterClockwise();
    else:
        rotateClockwise();

def verify_carrying_cone():
    coneDistance = getPingCenter();     # if the cone is close enough infront of us, transition phase to delivering
    print("cone distance: " + str(coneDistance))
    if (coneDistance < minConeCarryDistance and coneDistance != 0):
        return true
    else:
        return false

def look_for_cone():
    print("looking for cone");
    count = pixy_get_blocks(100, blocks)
    if (count > 0):
        for index in range (0, count):
            if (signature_cone_low <= blocks[index].signature <= signature_cone_high):
                print("Identified cone at x: " + str(blocks[index].x) + "y: " + str(blocks[index].y));
                move_towards_coordinate(blocks[index].x, blocks[index].y);
                if (verify_carrying_cone()):
                    print("Changing state to searching for delivery area")
                    state = delivering_cone
            break
    else: # no cones in field of view
        move_to_open_space()        # blind search in most open direction

def deliver_cone():
    if (not (verify_carrying_cone())):
        print("Cone is too far away, changing state to look for cone")
        state = looking_for_cone

    coneSigFound = false
    count = pixy_get_blocks(100, blocks)
    if (count > 0):
        for index in range (0, count):
            if (blocks[index].signature == signature_collection_box):
                print("Identified collection at x: " + str(blocks[index].x) + "y: " + str(blocks[index].y));
                move_towards_coordinate(blocks[index].x, blocks[index].y);

                # check y coordinate...
            if (blocks[index].signature == signature_cone_low):
                coneSigFound = true
        if (coneSigFound == false):
            print("Cone signature was not found, going back to looking for cone")
            state = looking_for_cone
    else: # no cones in field of view
        move_to_open_space()        # blind search in most open direction




while (1):

    distanceLeft = getPingLeft();
    distanceRight = getPingRight();

    if (objectDetected(distanceLeft) or
        objectDetected(distanceRight)):

	print("Evading object")
        if (objectDetected(distanceLeft)):
            rotateCounterClockwise();
        elif (objectDetected(distanceRight)):        
            rotateClockwise();

        while (objectDetected(distanceLeft) or
            objectDetected(distanceRight)):

            distanceLeft = getPingLeft();
            distanceRight = getPingRight();
        
        print("done")
        halt();
        move_to_open_space();
        
    else:
        move_to_open_space();
        if (state == looking_for_cone):
            look_for_cone();
        elif (state == delivering_cone):
            deliver_cone();

file.close();
