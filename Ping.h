#ifdef __cplusplus
extern "C" {
#endif

struct Ping {
  int digitalPinLeft;
  int digitalPinRight;
  int digitalPinCenter
};

#ifndef Ping_h
#define Ping_h

void init_Ping(int, int, int);
long getPingLeft();
long getPingRight();
long getPingCenter();



#endif

#ifdef __cplusplus
}
#endif
