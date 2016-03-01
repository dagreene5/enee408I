#ifdef __cplusplus
extern "C" {
#endif

struct Motor {
  int digitalPin1;
  int digitalPin2;
  int pwmPin;
  int digital1Low;
  int pwmVal;
  int setDelay;  
  
};

#ifndef Motor_h
#define Motor_h

void init_Motors(int, int, int, int, int, int);
void setLeftPWM(int);
void setRightPWM(int);
int getLeftPWM();
int getRightPWM();
void setPWMs(int);
void incrementLeft(int);
void incrementRight(int);
void setLeftForward();
void setLeftBackward();
void setRightForward();
void setRightBackward();
void setRotateClockwise();
void setRotateCounterClockwise();
void setMoveForward();
void setMoveBackward();
void halt();
void haltLeft();
void haltRight();



#endif

#ifdef __cplusplus
}
#endif
