import math
from Point import Point
import Tkinter as tk

# Robot shape
class Robot():
	def __init__(self, canvas):
		self.canvas = canvas
		self.center = Point(500, 500)
		self.angle = 0
		self.radius = 50
		self.x, self.y = self.center.x, self.center.y
		self.w1_angle, self.w2_angle, self.w3_angle = 0, 0, 0
		self.update()

	def turn(self, degrees):
		self.angle += math.radians(degrees)		

	def linear(self, speed):
		self.center = Point(self.x+speed*(math.sin(self.angle) * self.radius/2), self.y-speed*(math.cos(self.angle) * self.radius/2))

	def strafe(self, speed):
		self.center = Point(self.x+speed*(math.sin(math.pi/2 - self.angle) * self.radius/2), self.y+speed*(math.cos(math.pi/2 - self.angle) * self.radius/2))

	def linear_strafe_pos(self, speed):
		self.center = Point(self.x+speed*(math.sin(math.pi/4 - self.angle) * self.radius/2), self.y+speed*(math.cos(math.pi/4 - self.angle) * self.radius/2))

	def linear_strafe_neg(self, speed):
		self.center = Point(self.x+speed-(math.sin(math.pi/4 - self.angle) * self.radius/2), self.y+speed*(math.cos(math.pi/4 - self.angle) * self.radius/2))

	def update(self):
		print str(self.x) + ", " + str(self.y)
		self.x, self.y = self.center.x, self.center.y
		self.canvas.delete("all")

		# Chassis
		p1 = Point(self.x - self.radius*math.sin(self.angle + 4*math.pi/3.0), self.y + self.radius*math.cos(self.angle + 4*math.pi/3.0))
		p2 = Point(self.x - self.radius*math.sin(self.angle + 0), self.y + self.radius*math.cos(self.angle + 0))
		p3 = Point(self.x - self.radius*math.sin(self.angle + 2*math.pi/3.0), self.y + self.radius*math.cos(self.angle + 2*math.pi/3.0))
		self.canvas.create_line(p1.x, p1.y, p2.x, p2.y)
		self.canvas.create_line(p2.x, p2.y, p3.x, p3.y)
		self.canvas.create_line(p3.x, p3.y, p1.x, p1.y, fill="blue", width="2.0")

		# Wheels
		half_diagonal = self.radius/5

		# Wheel 1
		# w1 = canvas.create_rectangle(p1.x-half_diagonal/math.sqrt(3), p1.y-half_diagonal(math))