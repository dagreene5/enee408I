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

void setLeftPWM(int pwm) {
  leftMotor.pwmVal = pwm;
  analogWrite(leftMotor.pwmPin, leftMotor.pwmVal);
}
void setRightPWM(int pwm) {
  rightMotor.pwmVal = pwm;
  analogWrite(rightMotor.pwmPin, rightMotor.pwmVal);
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
  setLeftPWM(80);
  setRightBackward();
  setRightPWM(60);
}

void setRotateCounterClockwise() {
  setLeftBackward();
  setLeftPWM(100);
  setRightForward();
  setRightPWM(60);
}
void setMoveForward() {
  setLeftForward();
  setRightForward();
  setLeftPWM(100);
  setRightPWM(50);
}
void setMoveBackward() {
  setLeftBackward();
  setRightBackward();
  setLeftPWM(80);
  setRightPWM(80);
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

