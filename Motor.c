#include "Arduino.h"
#include "Motor.h"

static struct Motor all_motors[2];
static int numMotors;

struct Motor * init_Motor(int dig1, int dig2, int pwm) {
  if (numMotors >= 2) {
    return NULL;
  }

  struct Motor* motor = &all_motors[numMotors++];

  motor->digitalPin1 = dig1;
  motor->digitalPin2 = dig2;
  motor->pwmPin = pwm;
  motor->setDelay = 20;

  pinMode(motor->digitalPin1, OUTPUT);
  pinMode(motor->digitalPin2, OUTPUT);
  pinMode(motor->pwmPin, OUTPUT);
  digitalWrite(motor->digitalPin1, LOW);
  digitalWrite(motor->digitalPin2, HIGH);
  analogWrite(motor->pwmPin, 0);

  motor->digital1Low = 1;

  return motor;
}

void setPWM(struct Motor *motor, int pwm) {
  motor->pwmVal = pwm;
  analogWrite(motor->pwmPin, motor->pwmVal);
}

void reverseDirection(struct Motor *motor) {
  if (motor->digital1Low) {

    digitalWrite(motor->digitalPin1, HIGH);
    digitalWrite(motor->digitalPin2, LOW);
    
    motor->digital1Low = 0;
  } else {

    digitalWrite(motor->digitalPin1, LOW);
    digitalWrite(motor->digitalPin2, HIGH);
  
    motor->digital1Low = 1;
  }
}
