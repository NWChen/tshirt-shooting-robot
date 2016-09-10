#include <AccelStepper.h>
#include <Servo.h>

// *** *** *** *** OUTPUT *** *** *** ***
class Output {
  const boolean debug = false;
  public:
  Output() {
  }
  
  void printDebug(String id, String str) {
    if(debug)
      Serial.println(id + ": " + str);
  }
};

// *** *** *** *** CYLINDER *** *** *** ***
class Cylinder: public Output {
  AccelStepper* stepper;
  int switch_port;
  
  // Constructor
  public: 
  Cylinder(int _switch_port, int dir_pin1, int dir_pin2, float max_speed=200.0) {
    switch_port = _switch_port;
    pinMode(switch_port, INPUT);
    stepper = new AccelStepper(2, dir_pin1, dir_pin2);
    analogWrite(3, 100);
    analogWrite(11, 100);
    stepper -> setMaxSpeed(max_speed);
    stepper -> setAcceleration(max_speed/10.0);
  }
  
  // Index by the given number of chambers
  void index(int chambers=1) {
    stepper -> moveTo(chambers * 200); // gear ratio is 1:6, and 360/60 * 6 = 1, so 200*1 = 200 steps/chamber
    stepper -> run();
  }
  
  // Determine whether the cylinder has rotated the given number of chambers
  boolean hasRotated() {
    return stepper -> distanceToGo() == 0;
  }
  
  // Determine whether the limit switch is depressed
  boolean isAligned() {
    return digitalRead(switch_port) == 1;
  }
  
  // Conserves power for the stepper
  void release() {
    stepper -> disableOutputs();
  }
  
  // Stops the cylinder from rotating
  void stop() {
    stepper -> stop();
  }
  
  void printDebug() {
    Output::printDebug("CYLINDER", "foo");
  }
};

// *** *** *** *** RACK *** *** *** ***
class Rack: public Output {
  Servo servo;
  int pot_port;
  
  // Constructor
  public: 
  Rack(int _servo_port, int _pot_port) {
    servo.attach(_servo_port);
  }
  
  // Retract the rack away from the chamber
  void retract() {
    servo.write(45);
  }
  
  // Extend the rack towards the chamber
  void extend() {
    servo.write(145);
  }
  
  // Detect whether the rack is retracted
  boolean isRetracted() {
    return readPot() < 1;
  }

  // Detect whether the rack is extended
  boolean isExtended() {
    return readPot() > 99;
  }
  
  // Read the position of the rack
  int readPot() {
    return map(analogRead(pot_port), 23, 1000, 0, 100);
  }
  
  void printDebug() {
    Output::printDebug("RACK", "foo");
  }
};

// *** *** *** *** WHEEL *** *** *** ***
class Wheel: public Output {
  Servo servo;
  int reverse;
  int servo_port;
  
  // Constructor
  public: Wheel(int _servo_port, boolean _reverse=false) {
    if(_reverse)
      reverse = -1;
    else
      reverse = 1;
    servo_port = _servo_port;
    attach();
  }
  
  // Accelerate the wheel
  void spinUp() {
    attach();
    servo.write(90 + 90*reverse);
  }
  
  // Cut off power to the wheel
  void release() {
    servo.detach();
  }
  
  // Provide power to the wheel
  void attach() {
    servo.attach(servo_port);
  }
  
  void printDebug() {
    Output::printDebug("WHEEL", "foo");
  }
};

// *** *** *** *** INPUTS *** *** *** ***
class Inputs {
  // Constructor
  public: Inputs() {
  }
};

// *** *** *** *** MAIN *** *** *** ***
#define kLWHEEL_PORT 1
#define kRWHEEL_PORT 2
#define kSERVO_PORT 3
#define kPOT_PORT 4
#define kSWITCH_PORT 5
#define kDIR1_PORT 6
#define kDIR2_PORT 7

#define IDLE 0
#define CYLINDER_STOPPED 1
#define RACK_EXTENDING 2
#define RACK_RETRACTING 3
#define CYLINDER_ROTATING 4
#define CHAMBER_ALIGNED 5
#define CYLINDER_ADJUSTING 6

#define WHEEL_RELEASE 0
#define WHEEL_SPINUP 1

Wheel leftWheel(kLWHEEL_PORT);
Wheel rightWheel(kRWHEEL_PORT, true);
Rack rack(kSERVO_PORT, kPOT_PORT);
Cylinder cylinder(kSWITCH_PORT, kDIR1_PORT, kDIR2_PORT);
unsigned int fsm_state = 0;
unsigned int fsm2_state = 0;

void setup() {
}

void loop() {
  cylinder.printDebug();
  rack.printDebug();
  leftWheel.printDebug();
  rightWheel.printDebug();
  Serial.println(fsm_state);
  switch(fsm_state) {
    case IDLE:
      cylinder.release();
      fsm_state = CYLINDER_STOPPED;
      break;
    case CYLINDER_STOPPED:
      cylinder.stop();
      fsm_state = RACK_EXTENDING;
      break;
    case RACK_EXTENDING:
      if(rack.isExtended())
        fsm_state = RACK_RETRACTING;
      break;
    case RACK_RETRACTING:
      if(rack.isRetracted())
        fsm_state = CYLINDER_ROTATING;
      break;
    case CYLINDER_ROTATING:
      cylinder.index(1);
      if(cylinder.hasRotated())
        fsm_state = CHAMBER_ALIGNED;
      break;
    case CHAMBER_ALIGNED:
      if(cylinder.isAligned())
        fsm_state = IDLE;
      else
        fsm_state = CYLINDER_ADJUSTING;
      break;
    case CYLINDER_ADJUSTING:
      // ******* MISSING ADJUSTMENT CODE
      fsm_state = CHAMBER_ALIGNED;
      break;
  }
  
  switch(fsm2_state) {
     case WHEEL_RELEASE:
       leftWheel.release();
       rightWheel.release();
       break;
     case WHEEL_SPINUP:
       leftWheel.spinUp();
       rightWheel.spinUp();
       break;
  }
}

