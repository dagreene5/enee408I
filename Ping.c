#include "Ping.h"
#include "Arduino.h"

struct Ping ping;

void init_Ping(int digitalLeft, int digitalRight, int digitalCenter) {
  ping.digitalPinLeft = digitalLeft;
  ping.digitalPinRight = digitalRight;
  ping.digitalPinCenter = digitalCenter;
  pinMode(ping.digitalPinLeft, OUTPUT);
  pinMode(ping.digitalPinRight, OUTPUT);
  pinMode(ping.digitalPinCenter, OUTPUT);
}
void sendPulse(int pin) {
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pin, LOW);
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}

long getPingReading(int pin) {
  sendPulse(pin);
  pinMode(pin, INPUT);
  long duration = pulseIn(pin, HIGH, 10000);
  return microsecondsToCentimeters(duration);
}

long getPingLeft() {
  return getPingReading(ping.digitalPinLeft);
}

long getPingRight() {
  return getPingReading(ping.digitalPinRight);
}

long getPingCenter() {
  return getPingReading(ping.digitalPinCenter);
}



