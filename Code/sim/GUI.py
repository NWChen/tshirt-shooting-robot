import cmath, math, time
from Tkinter import *
from Drive import Drive
from Joystick import Joystick
from Point import Point
from Wheel import Wheel

"""
A GUI for swerve simulation and testing.
"""
class GUI(object):

	"""
	Creates a GUI instance.
	@type root: Tkinter.Tk()
	@param root: A Tkinter.Tk object
	@type canvas_width: number
	@param canvas_width: The width of the canvas, in pixels
	@type canvas_height: number
	@param canvas_height: The height of the canvas, in pixels
	@type radius: number
	@param radius: The length of the diagonal of the rectangle representing a wheel
	""" 
	def __init__(self, root, joystick=None, canvas_width=1000, canvas_height=1000, radius=20, wheel_diagonal=10):	
		self.joystick = joystick

		# Canvas on which to draw graphics
		self.w = Canvas(root, width=canvas_width, height=canvas_height)
		self.w.pack()
		self.drive = Drive(0, Point(canvas_width/2, canvas_height/2), radius)
		self.wheel_diagonal = wheel_diagonal
		self.s_wheels = []

		# Draw the chassis of the robot. "s" stands for "shape"
		self.s_drive = self.w.create_polygon(self.drive.wheels[0].center.x, self.drive.wheels[0].center.y,
																			self.drive.wheels[1].center.x, self.drive.wheels[1].center.y, 
																			self.drive.wheels[2].center.x, self.drive.wheels[2].center.y, fill="#3E3E3E")
		self.s_frontedge = self.w.create_line(self.drive.wheels[0].center.x, self.drive.wheels[0].center.y,
																			self.drive.wheels[1].center.x, self.drive.wheels[1].center.y, fill="#22A7F0", width=3.0)
		# Draw the wheels of the robot
		for wheel in self.drive.wheels:
			self.s_wheels.append(self.w.create_polygon(wheel.center.x-wheel_diagonal/4, wheel.center.y+math.sqrt(3)*wheel_diagonal/2,
																	wheel.center.x+wheel_diagonal/4, wheel.center.y+math.sqrt(3)*wheel_diagonal/2,
																	wheel.center.x+wheel_diagonal/4, wheel.center.y-math.sqrt(3)*wheel_diagonal/2,
																	wheel.center.x-wheel_diagonal/4, wheel.center.y-math.sqrt(3)*wheel_diagonal/2, stipple="gray75"))
		
	"""
	Animates the turning of the robot.
	@type speed: number
	@param speed: The speed at which the robot should turn
	"""
	def robot_turn(self, speed):
		self.drive.turn(speed)
		self.update_robot()
		for i in range(0, 3):
			self.build_rectangle(self.s_wheels[i], self.drive.center, self.drive.angle)
		self.w.update()

	"""
	Animates the translational crab motion of the robot.
	@type angle: number
	@param speed: The angle at which the robot should move
	@type speed: number
	@param speed: The speed at which the robot should move
	"""
	def robot_crab(self, angle, speed):
		self.drive.crab(angle, speed)
		self.update_robot()
		self.w.update()

	"""
	Redraws the robot on the field.
	"""
	def update_robot(self):
		self.w.coords(self.s_drive, self.drive.wheels[0].center.x, self.drive.wheels[0].center.y,
																	self.drive.wheels[1].center.x, self.drive.wheels[1].center.y, 
																	self.drive.wheels[2].center.x, self.drive.wheels[2].center.y)
		self.w.coords(self.s_frontedge, self.drive.wheels[0].center.x, self.drive.wheels[0].center.y,
																			self.drive.wheels[2].center.x, self.drive.wheels[2].center.y)

	"""
	Redraws a robot wheel.
	@type wr_angle: number
	@param wr_angle: The angle of the wheel to the robot's axis perpendicular to the front edge.
	"""
	def build_rectangle(self, shape, wheel, wr_angle=0):
		wf_angle = self.drive.angle - wr_angle # Angle of wheel to the field, where the north direction is 0
		dx = math.sin(wf_angle)*self.wheel_diagonal/2
		dy = math.cos(wf_angle)*self.wheel_diagonal/2
		w.coords(shape, wheel.center.x+)