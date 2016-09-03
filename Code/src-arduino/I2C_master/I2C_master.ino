#include <Wire.h>

class I2C_master {
  
  int slaveId;
  
  public:
  // Constructor
  I2C_master(int deviceId) {
    slaveId = deviceId;
    Wire.begin();
  }
  
  void transmit(int deviceId, byte message) {
    Wire.beginTransmission(deviceId);
    Wire.write(message);
    Wire.endTransmission();
  }
}
