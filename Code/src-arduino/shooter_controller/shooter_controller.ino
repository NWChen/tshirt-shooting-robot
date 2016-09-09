#include <AccelStepper.h>
#include <Servo.h>

// *** OUTPUT ***
class Output {
  const boolean debug = false;
  public:

    void printDebug(String id, String str) {
      if(debug) {
        Serial.println(id + ": " + str);
      }
    }
};

// *** CYLINDER ***
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
  
  boolean isAligned() {
    return digitalRead(switch_port) == 1;
  }
  
  // Stops the cylinder from rotating
  void stop() {
    stepper -> stop();
  }
  
  void printDebug() {
    Output::printDebug("CYLINDER", "foo");
  }
};

// *** RACK ***
class Rack: public Output {
  Servo servo;
  int pot_port;
  
  // Constructor
  public: 
  Rack(int _servo_port, int _pot_port) {
    servo.attach(_servo_port);
  }
  
  boolean retract() {
    return 
  }
  
  boolean extend() {
  
  }
  
  boolean isRetracted() {
    return readPot() < 1;
  }

  boolean isExtended() {
    return readPot() > 99;
  }
  
  int readPot() {
    return map(analogRead(pot_port), 23, 1000, 0, 100);
  }
  
  void printDebug() {
    Output::printDebug("RACK", "foo");
  }
};

// *** WHEEL ***
class Wheel {
  // Constructor
  public: Wheel() {
  }
};

// *** INPUTS ***
class Inputs {
  // Constructor
  public: Inputs() {
  }
};

void setup() {
}

void loop() {
}

