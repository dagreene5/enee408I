#include "Motor.h"
#include "string.h"

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
Motor *motor1, *motor2;

void setup() {

  Motor motor1_init(digital2, digital4, pwm5);
  motor1 = &motor1_init;
  motor1->initialize();

  Motor motor2_init(digital8, digital7, pwm3);
  motor2 = &motor2_init;
  motor2->initialize();

  motor1->setPWM(0);
  motor2->setPWM(0);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    char input = Serial.read();
    int pwmSpeed = 0;
    

    while (Serial.available() > 0) {
      Serial.read();
    }
    
    switch (input) {

      case 'g':
        Serial.print("read input: ");
        Serial.println(input);
        pwmSpeed = 50;
        break;
      case 's':
        pwmSpeed = 0;
        break;
    }

    Serial.print("pwm speed: ");
    Serial.println(pwmSpeed);

    analogWrite(pwm3, pwmSpeed);
    analogWrite(pwm5, pwmSpeed);
    /*motor2->setPWM(pwmSpeed);
    motor1->setPWM(pwmSpeed);*/
  
  }

  delay(500);
  
}



