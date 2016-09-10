#include <AccelStepper.h>
/* This Rugged Motor Driver application demonstrates the use of the AccelStepper
 * library for stepper motor control with ramp-up and ramp-down of speed.
 * The AccelStepper library can be downloaded from:
 *
 *     http://www.open.com.au/mikem/arduino/AccelStepper
 *
 * Assumptions:
 *   - bipolar stepper motor connected to the 2 phases
 *   - 8V-30V supply connected to Vin
 *   - Vin jumper is cut (J21) if Vin>15V (OK up to 24V for Ruggeduino)
 *
 * The behavior is as follows:
 *
 *   - The motor accelerates up to 300 steps per second for a total travel of 4000 steps
 *   - The motor then decelerates and reverses direction for another travel of 4000 steps
 *   - The process repeats
 * 
 * This software is licensed under the GNU General Public License (GPL) Version
 * 3 or later. This license is described at
 * http://www.gnu.org/licenses/gpl.html
 *
 * Application Version 1.0 -- October 2011 Rugged Circuits LLC
 * http://ruggedcircuits.com
 */
 
// Define an AccelStepper object controlling direction pins D12 and D13 (default
// Rugged Motor Driver connections)
AccelStepper stepper1(2,12,13);

void setup()
{ 
  // Set power on pins D3 and D11, the ENABLE1 and ENABLE2 pins. The parameter
  // is in the range 0 (no power) to 255 (maximum power).
    analogWrite(3, 100);
    analogWrite(11, 100);

  // Set step speed in steps per second
    stepper1.setMaxSpeed(300.0);

  // Set acceleration/deceleration in steps per second per second
    stepper1.setAcceleration(300.0);

  // Begin motion
    stepper1.moveTo(86);

  // Change from divide-by-64 prescale on Timer 2 to divide by 8 to get
  // 8-times faster PWM frequency (976 Hz --> 7.8 kHz). This should prevent
  // overcurrent conditions for steppers with high voltages and low inductance.
  TCCR2B = _BV(CS21);
}
 
void loop()
{
  // Once the motor has reached its target position, decelerate and move to the
  // same position in the other direction.
    if (stepper1.distanceToGo() == 0) {
      stepper1.moveTo(stepper1.currentPosition() + 171);
    }
    stepper1.run();
}
// vim: syntax=c cindent expandtab ts=2 sw=2
