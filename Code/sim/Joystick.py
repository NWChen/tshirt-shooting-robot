import os, sys
import math
import pygame
import time
from pygame.locals import *

"""
Implements a USB joystick.
"""
class Joystick(object):

	# constants
	AXIS_PRECISION = 2 # decimal places
	INIT_X, INIT_Y, INIT_R, INIT_T = 0, 0, 0, 0 # zero values for each axis
	X_AXIS, Y_AXIS, R_AXIS, T_AXIS = 0, 1, 3, 2

	# TODO: Implement multiple joystick/non-Freedom2.4 compatibility
	"""
	Creates a Joystick object.
	"""	
	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()
		self.INIT_X, self.INIT_Y, self.INIT_R, self.INIT_T = self.joystick.get_axis(self.X_AXIS), self.joystick.get_axis(self.Y_AXIS), \
																												self.joystick.get_axis(self.R_AXIS), self.joystick.get_axis(self.T_AXIS)

	"""
	Returns the value of the joystick's X axis.
	@rtype: number
	@return: the value of the X axis between -1.0 (left) and 1.0 (right)
	"""	
	def get_x(self):
		pygame.event.pump()
		return round(self.joystick.get_axis(self.X_AXIS), self.AXIS_PRECISION) - self.INIT_X

	"""
	Returns the value of the joystick's Y axis.
	@rtype: number
	@return: the value of the Y axis between -1.0 (backwards) and 1.0 (forwards)
	"""	
	def get_y(self):
		pygame.event.pump()
		return -round(self.joystick.get_axis(self.Y_AXIS), self.AXIS_PRECISION) - self.INIT_Y

	"""
	Returns the value of the joystick's vertical rotational axis.
	@rtype: number
	@return: the value of the rotational axis between -1.0 (left) and 1.0 (right)
	"""	
	def get_r(self):
		pygame.event.pump()
		return round(self.joystick.get_axis(self.R_AXIS), self.AXIS_PRECISION) - self.INIT_R

	"""
	Returns the value of the joystick's throttle axis.
	@rtype: number
	@return: the value of the rotational axis between 0.0 (bottom) and 1.0 (top)
	"""	
	def get_throttle(self):
		pygame.event.pump()
		return self.map_to_full_range(round(self.joystick.get_axis(self.T_AXIS), self.AXIS_PRECISION) - self.INIT_T, -1.0, 1.0, 1.0, 0.0)

	"""
	Returns the value of the joystick's angle relative to the neutral position.
	@rtype: number
	@return: the value of the joystick's angle between -pi and pi
	"""	
	def get_angle(self):
		pygame.event.pump()
		try:
			return round(math.atan2(self.get_y(), self.get_x())-math.radians(90), self.AXIS_PRECISION)
		except ZeroDivisionError:
			return 0.0

	"""
	Returns the magnitude of the Joystick's position relative to the neutral position.
	@rtype: number
	@return: the magnitude of the Joystick's position between 0.0 and 1.0
	"""	
	def get_magnitude(self):
		pygame.event.pump()
		return round(math.sqrt(self.get_x()**2 + self.get_y()**2), self.AXIS_PRECISION)

	@staticmethod
	def map_to_full_range(x, in_min, in_max, out_min=-1.0, out_max=1.0):
		return ((x-in_min)*(out_max-out_min)) / (in_max-in_min)+out_min