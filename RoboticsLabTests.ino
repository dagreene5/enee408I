#include "Motor.h"
#include "string.h"
#include "Ping.h"

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


void setup() {

  // left pins, then right pins
  init_Motors(digital2, digital4, pwm5,
    digital8, digital7, pwm3);
  init_Ping(digital12);
  Serial.begin(9600);
}

void loop() {


  //travelInSquare();
  //testPing();  
  moveAround();
  
}

void testPing() {
  Serial.print("Ping reading: ");
  Serial.println(getPingReading());
  delay(500);
}

void moveAround() {

  int pingReading = getPingReading();
  long minDistance = 20;
  
  if (pingReading < minDistance && pingReading != 0) {
    halt();

    while ((pingReading = getPingReading()) < minDistance && pingReading != 0) {
      setRotateClockwise();
      delay(100);
    }

    halt();
    delay(100);
    setMoveForward();
  } else {
    setMoveForward();
  }

  delay(100);
}

void readFromSerial() {
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
        setPWMs(pwmSpeed);
        break;
      case 's':
        pwmSpeed = 0;
        setPWMs(pwmSpeed);
        break;
    } 
  }
}

void travelInSquare() {

  setMoveForward();
  delay(3000);
  halt();
  delay(200);
  setRotateClockwise();
  delay(1000);
  halt();
  delay(200);
  setMoveForward();
  delay(3000);
  halt();
  delay(200);
  setRotateClockwise();
  delay(1000);
  halt();
  delay(200);
  setMoveForward();
  delay(3000);
  halt();
  delay(200);
  setRotateClockwise();
  delay(1000);
  halt();
  delay(200);
}



