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

struct Motor *init_Motor(int, int, int);
void setPWM(struct Motor *, int);
void reverseDirection(struct Motor *);



/*
class Motor {
  int digital1, digital2, pwm;
  int digital1Low;
  int pwmVal;
  int setDelay;
  
  public:
    Motor(int, int, int);     // set digital and pwm pins
    void initialize();             // set pin modes and digital HIGH/LOW
    void setPWM(int);              // set speed
    void reverseDirection();       // flip digital outputs
};*/

#endif

#ifdef __cplusplus
}
#endif
