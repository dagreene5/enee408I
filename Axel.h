#ifdef __cplusplus
extern "C" {
#endif

struct Axel {
  struct Motor *leftMotor;
  struct Motor *rightMotor; 
};

#ifndef Axel_h
#define Axel_h

struct Axel *init_Axel(struct Motor *, struct Motor *);
int incrementLeft(struct Axel *, int);
int incrementRight(struct Axel *, int);

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
