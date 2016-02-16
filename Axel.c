#include "Axel.h"
#include "Motor.h"
#include "Arduino.h"

struct Axel axel;

struct Axel *init_Axel(struct Motor * left, struct Motor * right) {
  axel.leftMotor = left;
  axel.rightMotor = right;

  return &axel;
}

int incrementMotor(struct Motor *motor, int increment) {

  int pwmVal = motor->pwmVal;
  
  pwmVal += increment;

  if (pwmVal < 0) {
    pwmVal = 0;
  } else if (pwmVal > 255) {
    pwmVal = 255;
  }
  
  setPWM(motor, pwmVal);

  return pwmVal;
}

int incrementLeft(struct Axel *axel, int increment) {
  return incrementMotor(axel->leftMotor, increment);
}
int incrementRight(struct Axel *axel, int increment) {
  return incrementMotor(axel->rightMotor, increment);
}



