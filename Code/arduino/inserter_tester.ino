#include <Servo.h>

Servo myservo;
int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(6);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  myservo.write(60);
  delay(1000);
  myservo.write(235);
  delay(500);
}

