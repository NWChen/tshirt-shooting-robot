from Joystick import Joystick
import time

joystick = Joystick()
while True:
	print joystick.get_x(), joystick.get_y(), joystick.get_r(), joystick.get_throttle()
	time.sleep(0.05)