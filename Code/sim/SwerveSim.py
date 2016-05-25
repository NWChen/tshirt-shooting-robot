from GUI import GUI
from Joystick import Joystick
from Tkinter import *

root = Tk()
root.title("Tribot Swerve Simulator")

joystick = Joystick()
gui = GUI(root, joystick, 1000, 1000, 40, 10)

def foo():
	while True:
		gui.robot_turn(joystick.get_r())
		gui.robot_crab(joystick.get_angle(), joystick.get_magnitude())

root.bind("<Visibility>", foo())
root.mainloop()
