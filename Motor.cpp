#include "Arduino.h"
#include "Motor.h"

Motor::Motor(int dig1, int dig2, int p) {
  digital1 = dig1;
  digital2 = dig2;
  pwm = p;
  setDelay = 20;
}

void Motor::initialize() {

  pinMode(digital1, OUTPUT);
  pinMode(digital2, OUTPUT);
  pinMode(pwm, OUTPUT);
  digitalWrite(digital1, LOW);
  digitalWrite(digital2, HIGH);

  digital1Low = 1;
}

void Motor::reverseDirection() {

  if (digital1Low) {

    digitalWrite(digital1, HIGH);
    digitalWrite(digital2, LOW);
    
    digital1Low = 0;
  } else {

    digitalWrite(digital1, LOW);
    digitalWrite(digital2, HIGH);
  
    digital1Low = 1;
  }
}

void Motor::setPWM(int val) {
  pwmVal = val;
  analogWrite(pwm, pwmVal);
}


