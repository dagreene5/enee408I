#ifdef __cplusplus
extern "C" {
#endif

struct Ping {
  int digitalPin;
};

#ifndef Ping_h
#define Ping_h

void init_Ping(int);
void sendPulse();
long getPingReading();



#endif

#ifdef __cplusplus
}
#endif
