import math
from Point import Point

"""
Implements an independent swerve module as a wheel.
"""
class Wheel(object):

	"""
	Creates a Wheel object.
	@type center: Point
	@param center: The center of mass of the rectangle representing the wheel's shape
	@type speed: number
	@param speed: The speed with which the wheel moves
	"""
	def __init__(self, center=Point(0,0), speed=0.0):
		self.angle = 0.0 # angle to the axis perpendicular to the forward-facing edge of the chassis
		self.angle_to_field = 0.0 # angle to the axis perpendicular to the top edge of the field
		self.center = center
		self.speed = speed

	"""
	Sets the speed of the wheel from a range of -1.0 to 1.0.
	@type speed: number
	@param speed: The speed of the wheel
	"""
	def set_speed(self, speed):
		if speed < -1.0:
			self.speed = -1.0
		elif speed > 1.0:
			self.speed = 1.0
		else:
			self.speed = speed

	"""
	Sets the angle of the wheel relative to the chassis of the robot.
	"""
	def set_angle(self, angle):
		self.angle = angle % 360

	"""
	Sets the angle of the wheel relative to the field.
	"""
	def set_angle_to_field(self, angle_to_field):
		self.angle_to_field = angle_to_field % 360
