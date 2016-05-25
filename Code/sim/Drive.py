import math
from Point import Point
from Wheel import Wheel

'''
Implements a 3-wheel swerve drivetrain, with wheels at
each vertex of an equilateral triangle.
'''
class Drive(object):

	"""
	Creates a drivetrain object.
	"""
	def __init__(self, angle=0, center=Point(0,0), radius=20, speed_divider=6):
		self.angle = angle
		self.center = center
		self.radius = radius
		self.speed_divider = speed_divider

		# Drivetrain wheels
		w0 = Wheel(Point(center.x-radius*(math.sqrt(3)/2), center.y-radius/2))
		w1 = Wheel(Point(center.x+radius*(math.sqrt(3)/2), center.y-radius/2))
		w2 = Wheel(Point(center.x, center.y+radius))
		self.wheels = [w0, w1, w2]

	"""
	Turn the drivetrain in place.
	@type speed: number
	@param speed: The speed at which the drivetrain rotates. A positive speed causes clockwise rotation; a negative speed causes counterclockwise rotation.
	"""
	def turn(self, speed):
		self.angle += math.radians(speed/self.speed_divider)
		self.gen_wheels()
		self.set_angle(60, -60, 90)
		self.set_speed(speed, speed, speed)

	"""
	Translate the drivetrain linearly. All wheels have the same velocity.
	@type angle: number
	@param angle: The angle of the wheels, relative to the front edge of the robot
	@type speed: number
	@param speed: The speed at which the drivetrain moves
	"""
	def crab(self, angle, speed):
		speed = speed/self.speed_divider
		adjusted_angle = (math.radians(90)-self.angle)#%(2*math.pi)
		self.center.x = self.center.x+speed*(math.cos(angle+adjusted_angle))
		self.center.y = self.center.y-speed*(math.sin(angle+adjusted_angle))
		self.gen_wheels()
		self.set_angle(angle, angle, angle)
		self.set_speed(speed, speed, speed)

	"""
	Stop the drivetrain, and face all wheels to the forward edge of the drivetrain.
	"""
	def zero():
		self.set_angle(0, 0, 0)
		self.set_speed(0.0, 0.0, 0.0)

	"""
	Class method to set all wheels to a given angle.
	"""
	def set_angle(self, w0_angle, w1_angle, w2_angle):
		self.wheels[0].set_angle(w0_angle)
		self.wheels[1].set_angle(w1_angle)
		self.wheels[2].set_angle(w2_angle)

	"""
	Class method to set all wheels to a given speed.
	"""
	def set_speed(self, w0_speed, w1_speed, w2_speed):
		self.wheels[0].set_speed(w0_speed)
		self.wheels[1].set_speed(w1_speed)
		self.wheels[2].set_speed(w2_speed)

	"""
	Class method to redraw all wheels.
	"""
	def gen_wheels(self):
		default_offset = 0#-math.pi/2
		self.wheels = [Wheel(Point(self.center.x-self.radius*math.sin(self.angle+default_offset+2*math.pi/3.0), self.center.y+self.radius*math.cos(self.angle+default_offset+2*math.pi/3.0))),
								Wheel(Point(self.center.x-self.radius*math.sin(self.angle+default_offset+0), self.center.y+self.radius*math.cos(self.angle+default_offset+0))),
								Wheel(Point(self.center.x-self.radius*math.sin(self.angle+default_offset+4*math.pi/3.0), self.center.y+self.radius*math.cos(self.angle+default_offset+4*math.pi/3.0)))]

