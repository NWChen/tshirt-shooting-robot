#include <Servo.h>

Servo inserter;
Servo indexer;

void setup() {
  // put your setup code here, to run once:
  inserter.attach(10);
  indexer.attach(11);
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  String s = Serial.readString();
  if(s != "") {
    if(s.substring(0,1) == "a")
      inserter.write(s.substring(1).toInt());
    else
      indexer.write(s.toInt());
  }
  Serial.println(s);
}
