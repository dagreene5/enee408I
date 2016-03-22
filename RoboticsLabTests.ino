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

String serialInput;


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
  readFromSerial();
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

    while (Serial.available() > 0) {
      char received = Serial.read();

      // end of command
      if (received == 'e') {

        executeCommand(serialInput);
        serialInput = "";
        
      } else {
        serialInput += received;
      }
    }
}

/*
 * commands:
 * 
 * sl # : set left to pwm #
 * il # : increment left by #
 * slb : set left backward
 * slf : set left forward
 * gl : get left pwm #
 * 
 * 
 * sr # : set right to pwm #
 * ir # : increment right by #
 * srb : set right backward
 * srf : set right forward
 * gr : get right pwm #
 * 
 * sb # : set both to pwm #
 * h : halt, equivalent to sb 0
 * 
 * smcw : set move clockwise
 * smcc : set move counterclockwise
 * smf : set move forward
 * smb : set move backward
 * 
 * gp : get ping reading
 */
void executeCommand(String command) {

  int pwmSpeed;
  
  switch (command[0]) {

      case 'i':
        switch (command[1]) {
          case 'l':
            incrementLeft(command.substring(3).toInt());
          break;

          case 'r':
            incrementRight(command.substring(3).toInt());
          break;
        }


        break;
      case 'g':

        switch (command[1]) {

          case 'r': // gr: get right pwm speed
            Serial.println(getRightPWM());
            Serial.flush();
          break;

          case 'l': // gl: get left pwm speed
            Serial.println(getLeftPWM());
            Serial.flush();
          break;

          case 'p': // gp: get ping reading
            Serial.println(getPingReading());
            Serial.flush();
          break;
        }
        
        break;
      case 's':
      
        switch (command[1]) {

          case 'r': 

            switch (command[2]) {

              case ' ': // sr #: set right motor to pwm #
                pwmSpeed = command.substring(3).toInt();
                setRightPWM(pwmSpeed);
               break;

              case 'b': // srb: set right backwards
                setRightBackward();
                break;
              case 'f': // srf: set right forward
                setRightForward();
                break;
            }
            
          break;

          case 'l': 
          
            switch (command[2]) {

              case ' ': // sl #: set left motor to pwm #
                pwmSpeed = command.substring(3).toInt();
                setLeftPWM(pwmSpeed);
               break;

              case 'b': // slb: set left backwards
                setLeftBackward();
                break;
              case 'f': // slf: set left forward
                setLeftForward();
                break;
            }
          break;

          case 'b': // sb #: set both motors to pwm #
            pwmSpeed = command.substring(3).toInt();
            setPWMs(pwmSpeed);
          break;

          case 'm': 

            switch (command[2]) {


              case 'c':

                switch(command[3]) {
                  
                  case 'w': // smcw : set clockwise
                    setRotateClockwise();
                    break;
  
                  case 'c': // smcc : set counterclockwise
                    setRotateCounterClockwise();
                    break;
                }
                break;

              case 'f':
                  setMoveForward();
                  break;
              case 'b':
                  setMoveBackward();
                  break;      
            }
            break;    
        }
        break;

      case 'h':
        halt();
        break;
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



