#include "Motor.h"
#include "string.h"
#include "Axel.h"

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

/* PWM Control Vars */
int powerDirection = 1;

/*
 * PWM 0 - 255
 */

 /*
  * As is, motor 2 is the right motor, motor1 is left.
  * Both are configured to start moving forward.
  */
struct Motor *motor1, *motor2;
struct Axel *axel;

void setup() {

  motor1 = init_Motor(digital2, digital4, pwm5);
  motor2 = init_Motor(digital8, digital7, pwm3);
  axel = init_Axel(motor1, motor2);

  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    char input = Serial.read();
    int pwmSpeed = 0;
    

    while (Serial.available() > 0) {
      Serial.read();
    }

    Serial.print("read input: ");
    Serial.println(input);
    switch (input) {

      case 'g':
        
        pwmSpeed = 50;
        setPWM(motor1, pwmSpeed);
        setPWM(motor2, pwmSpeed);
        break;
      case 's':
        pwmSpeed = 0;
        setPWM(motor1, pwmSpeed);
        setPWM(motor2, pwmSpeed);
        break;
      case 'l':

        int val;
        Serial.println("decreasing left");
        while ((val = incrementLeft(axel, -5)) != 0) {
          Serial.print("inc val: ");
          Serial.println(val);
          delay(20);
        }
        Serial.println("increasing right");
        while ((val = incrementRight(axel, 5)) != 255) {
          Serial.print("inc val: ");
          Serial.println(val);
          delay(20);
        }
        Serial.println("done");
        break;
      case 'r':
       Serial.println("increasing left");
        while (incrementLeft(axel, 5) != 255) {
          delay(20);
        }
        Serial.println("decreasing right");
        while (incrementRight(axel, -5) != 0) {
          delay(20);
        }
        Serial.println("done");
        break;
    }
    
    //analogWrite(pwm3, pwmSpeed);
    //analogWrite(pwm5, pwmSpeed);
    /*motor2->setPWM(pwmSpeed);
    motor1->setPWM(pwmSpeed);*/
  
  }

  delay(500);
  
}



