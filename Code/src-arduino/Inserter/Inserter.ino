#include <Servo.h>

class Inserter {

   boolean ENABLE_DEBUG = true;
   
   const short FORWARD_SPEED = 45;
   const short BACKWARD_SPEED = 145;
   const short STOP_SPEED = 90;
   const short FORWARD_POT_LIMIT = 0;
   const short BACKWARD_POT_LIMIT = 1023;
   int POT_PORT;
   Servo servo;
   
   public:
   // Constructor
   Inserter(int servoPort, int potPort) {
     POT_PORT = potPort;
     servo.attach(servoPort);
   }
   
   void moveForward() {
     while(analogRead(POT_PORT) > FORWARD_POT_LIMIT)
       rawMoveForward();
     stop();
   }
   
   void rawMoveForward() {
     servo.write(FORWARD_SPEED);
   }
   
   void rawMoveBackward() {
     servo.write(BACKWARD_SPEED);
   }
  
   void stop() {
     servo.write(STOP_SPEED);
   }
};
