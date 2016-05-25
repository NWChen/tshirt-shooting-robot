from Drive import Drive
import math

def assert_wheels():
	assert math.fabs(drive.wheels[0].speed <= 1.0)
	assert math.fabs(drive.wheels[1].speed <= 1.0)
	assert math.fabs(drive.wheels[2].speed <= 1.0)
	assert drive.wheels[0].angle > 0 or drive.wheels[0].angle < 360
	assert drive.wheels[1].angle > 0 or drive.wheels[1].angle < 360
	assert drive.wheels[2].angle > 0 or drive.wheels[2].angle < 360

drive = Drive()
for i in range(10**3):
	drive.turn(math.sin(i*(math.pi/36)))
	assert_wheels()
	drive.crab(i, math.sin(i*(math.pi/36)))
	assert_wheels()
print "Passed"