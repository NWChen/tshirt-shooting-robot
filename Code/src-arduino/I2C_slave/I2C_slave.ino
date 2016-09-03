#include <Wire.h>

class I2C_slave {
  
  byte message;
  
  public:
  // Constructor
  I2C_slave(int deviceId) {
    Wire.begin(deviceId);
    Wire.onReceive(receiveEvent);
  }
  
  void receiveEvent(int bytes) {
    message = Wire.read();
  }
  
}
