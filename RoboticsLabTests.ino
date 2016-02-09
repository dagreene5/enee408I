#include "Motor.h"

/* Digital Pins */
int digital2 = 2;
int digital4 = 4;
int digital7 = 7;
int digital8 = 8;
int digital12 = 12;
int digital13 = 13;

/* PWM Pins */
int pwm3 = 3;
int pwm5 = 5;
int pwm6 = 6;
int pwm9 = 9;
int pwm10 = 10;
int pwm11 = 11;

/* Analog Pins */
int analog0 = A0; //yellow or A
int analog1 = A1; //white or B
int analog2 = A2;
int analog3 = A3;
int analog4 = A4;
int analog5 = A5;

/* PWN Control Vars */
int pwmVal = 0;
int powerDirection = 1;

/*
 * PWM 0 - 255
 */
Motor *motor1, *motor2;

void setup() {

  Motor motor1_init(digital2, digital4, pwm5);
  motor1 = &motor1_init;
  motor1->initialize();

  Motor motor2_init(digital7, digital8, pwm3);
  motor2 = &motor2_init;
  motor2->initialize();
  
  Serial.begin(9600);
}

void loop() {
  motor1->setPWM(255);
  motor2->setPWM(255);
}

void readEncoders() {

  Serial.print("PWM val: ");
  Serial.println(pwmVal);
  int a_reading = analogRead(A0);
  int b_reading = analogRead(A1);
  Serial.print("A reading: ");
  Serial.println(a_reading);
  Serial.print("B reading: ");
  Serial.println(b_reading);
  Serial.println();
}

void testMotors() {
  pwmVal += (10 * powerDirection);

  if (pwmVal > 255) {
    pwmVal = 255;
    powerDirection = -powerDirection;
  } else if (pwmVal < 0) {
    pwmVal = 0;
    digitalWrite(digital7, HIGH);
    digitalWrite(digital8, LOW);
    powerDirection = -powerDirection;
  }

  analogWrite(pwm3, pwmVal);
  analogWrite(pwm5, pwmVal);

  readEncoders();
  delay(5000);
 }

