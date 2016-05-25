#include <Servo.h>

#define k_mLeft 10
#define k_mRight 9
#define k_pSpeed A0

Servo left;
Servo right;
double speed;

void setup() {
  Serial.begin(9600);
  left.attach(k_mLeft);
  right.attach(k_mRight);
}

void loop() {
  speed = (double)map(analogRead(k_pSpeed), 0, 1023, 90, 180);
  if(speed<110) speed=90;
  left.write(speed);
  right.write(180-speed);
  Serial.println(String(speed) + ", " + String(180-speed));
}

