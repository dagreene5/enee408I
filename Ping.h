#ifdef __cplusplus
extern "C" {
#endif

struct Ping {
  int digitalPinLeft;
  int digitalPinRight;
};

#ifndef Ping_h
#define Ping_h

void init_Ping(int, int);
long getPingLeft();
long getPingRight();



#endif

#ifdef __cplusplus
}
#endif
