#include "Arduino.h"
#include "Motor.h"

static struct Motor leftMotor, rightMotor;

void init_Motors(int dig1Left, int dig2Left, int pwmLeft,
  int dig1Right, int dig2Right, int pwmRight) {

   leftMotor.digitalPin1 = dig1Left;
   leftMotor.digitalPin2 = dig2Left;
   leftMotor.pwmPin = pwmLeft;
   rightMotor.digitalPin1 = dig1Right;
   rightMotor.digitalPin2 = dig2Right;
   rightMotor.pwmPin = pwmRight;

   pinMode(leftMotor.digitalPin1, OUTPUT);
   pinMode(leftMotor.digitalPin2, OUTPUT);
   pinMode(leftMotor.pwmPin, OUTPUT);
   digitalWrite(leftMotor.digitalPin1, LOW);
   digitalWrite(leftMotor.digitalPin2, HIGH);
   analogWrite(leftMotor.pwmPin, 0);

   pinMode(rightMotor.digitalPin1, OUTPUT);
   pinMode(rightMotor.digitalPin2, OUTPUT);
   pinMode(rightMotor.pwmPin, OUTPUT);
   digitalWrite(rightMotor.digitalPin1, LOW);
   digitalWrite(rightMotor.digitalPin2, HIGH);
   analogWrite(rightMotor.pwmPin, 0);
   
   leftMotor.digital1Low = 1;
   rightMotor.digital1Low = 1;
}

void incrementLeft(int increment) {
  leftMotor.pwmVal += increment;
  if (leftMotor.pwmVal < 0) {
    leftMotor.pwmVal = 0;
  } else if (leftMotor.pwmVal > 255) {
    leftMotor.pwmVal = 255;
  }

  analogWrite(leftMotor.pwmPin, leftMotor.pwmVal);
}

void incrementRight(int increment) {
  rightMotor.pwmVal += increment;
  if (rightMotor.pwmVal < 0) {
    rightMotor.pwmVal = 0;
  } else if (rightMotor.pwmVal > 255) {
    rightMotor.pwmVal = 255;
  }

  analogWrite(rightMotor.pwmPin, rightMotor.pwmVal);
}

void setLeftPWM(int pwm) {
  leftMotor.pwmVal = pwm;
  analogWrite(leftMotor.pwmPin, leftMotor.pwmVal);
}
void setRightPWM(int pwm) {
  rightMotor.pwmVal = pwm;
  analogWrite(rightMotor.pwmPin, rightMotor.pwmVal);
}

int getLeftPWM() {
  return leftMotor.pwmVal;
}

int getRightPWM() {
  return rightMotor.pwmVal;
}
void setPWMs(int pwm) {
  setLeftPWM(pwm);
  setRightPWM(pwm);
}

void setLeftForward() {
   digitalWrite(leftMotor.digitalPin1, LOW);
   digitalWrite(leftMotor.digitalPin2, HIGH);  
   leftMotor.digital1Low = 1;
}
void setLeftBackward() {
   digitalWrite(leftMotor.digitalPin1, HIGH);
   digitalWrite(leftMotor.digitalPin2, LOW);  
   leftMotor.digital1Low = 0;
}
void setRightForward() {
   digitalWrite(rightMotor.digitalPin1, LOW);
   digitalWrite(rightMotor.digitalPin2, HIGH);  
   rightMotor.digital1Low = 1;
}
void setRightBackward() {
   digitalWrite(rightMotor.digitalPin1, HIGH);
   digitalWrite(rightMotor.digitalPin2, LOW);  
   rightMotor.digital1Low = 0;
}
void setRotateClockwise() {
  setLeftForward();
  setRightBackward();
}

void setRotateCounterClockwise() {
  setLeftBackward();
  setRightForward();
}
void setMoveForward() {
  setLeftForward();
  setRightForward();
}
void setMoveBackward() {
  setLeftBackward();
  setRightBackward();
}
void halt() {
  setPWMs(0);
}
void haltLeft() {
  setLeftPWM(0);
}
void haltRight() {
  setRightPWM(0);
}

