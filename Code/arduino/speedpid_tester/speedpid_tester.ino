#include <Stepper.h>

#define SENSOR_PIN A0
#define MOTOR_PWM_PIN 3
#define MOTOR_DIR_PIN 12

unsigned long prevTime;
double input, output, setpoint;
double errorSum, prevError;
double kP, kI, kD;
double deltaTime = 1;
int prevRotationInput = 0;

void setup() {
  Serial.begin(9600);

  // configure motor
  pinMode(MOTOR_PWM_PIN, OUTPUT);
  pinMode(MOTOR_DIR_PIN, OUTPUT);
  digitalWrite(MOTOR_PWM_PIN, LOW);
  digitalWrite(MOTOR_DIR_PIN, LOW);
  analogWrite(MOTOR_PWM_PIN, 0);

  // pid constants
  kP = 1;
  kI = 0;
  kD = 0;
  
  setMotor(100);
}

void loop() {
  int rotationInput = prevRotationInput + map(analogRead(SENSOR_PIN), 41, 981, 0, 360); // position of position sensor
  setpoint = 100;

  // compute update time interval
  unsigned long currTime = millis();
  deltaTime = (double) (currTime - prevTime);

  input = (rotationInput - prevRotationInput)/deltaTime;

  // compute errors
  double error = setpoint - input;
  errorSum += (error * deltaTime);
  double dError = (error - prevError) / deltaTime;

  // compute output
  output = kP * error;// + kI * errorSum + kD * dError;
  setMotor(output);
  Serial.println(String(input) + ", " + String(output) + ", " + String(error));

  // reset values
  prevError = error;
  prevTime = currTime;
  prevRotationInput = rotationInput;
}

void setMotor(int value) {
  if(value > 255) value = 255;
  if(value < 0) digitalWrite(MOTOR_DIR_PIN, HIGH);
  else digitalWrite(MOTOR_DIR_PIN, LOW);
  
  value = value/4;
  analogWrite(MOTOR_PWM_PIN, abs(value));
}
