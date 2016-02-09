#ifndef Motor_h
#define Motor_h

#include "Arduino.h"

class Motor {
  int digital1, digital2, pwm;
  int digital1Low;
  int pwmVal;
  int setDelay;
  
  public:
    Motor(int, int, int);     // set digital and pwm pins
    void initialize();             // set pin modes and digital HIGH/LOW
    void setPWM(int);              // set speed
    void reverseDirection();       // flip digital outputs
};

#endif
