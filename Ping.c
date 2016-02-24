#include "Ping.h"
#include "Arduino.h"

struct Ping ping;

void init_Ping(int digital) {
  ping.digitalPin = digital;
  pinMode(ping.digitalPin, OUTPUT);
}
void sendPulse() {
  pinMode(ping.digitalPin, OUTPUT);
  digitalWrite(ping.digitalPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ping.digitalPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(ping.digitalPin, LOW);
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}

long getPingReading() {
  sendPulse();
  pinMode(ping.digitalPin, INPUT);
  long duration = pulseIn(ping.digitalPin, HIGH, 10000);
  return microsecondsToCentimeters(duration);
}

