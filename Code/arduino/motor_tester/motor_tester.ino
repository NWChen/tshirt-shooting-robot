#include <Servo.h>

int motorPin = 7;
int value = 0;
Servo motor;

void setup() {
  Serial.begin(9600);
  pinMode(motorPin, OUTPUT);
  motor.attach(motorPin);
}

void loop() {
  value = 180;
  vexMotorWrite(motor, 200);
  Serial.println(String(value));
  delay(1000);
}

void setMotorA(int speed) {
  int motorSpeed = constrain(abs(speed), 0, 255);
  if(speed > 0)
    digitalWrite(DIR_A, HIGH);
  else
    digitalWrite(DIR_A, LOW);
  analogWrite(PWM_A, motorSpeed);
}

void setMotorB(int speed) {
  int motorSpeed = constrain(abs(speed), 0, 255);
  if(speed > 0)
    digitalWrite(DIR_B, HIGH);
  else
    digitalWrite(DIR_B, LOW);
  analogWrite(PWM_B, motorSpeed);
}

void vexMotorWrite(Servo motorObj, int speed) { 
  motorObj.write(map(speed, -255, 255, 1000, 2000));
}
