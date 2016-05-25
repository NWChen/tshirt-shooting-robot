from Wheel import Wheel
import math

wheel = Wheel()
for i in range(10**3):
	wheel.set_speed(math.sin(i*(math.pi/36)))
	wheel.set_angle(i)
	assert math.fabs(wheel.speed) <= 1.0
	assert wheel.angle > 0 or wheel.angle < 360
print "Passed"