import Tkinter as tk

import Display as display
from Robot import Robot

root = tk.Tk()
root.resizable(width=False, height=False)
application = display.Display(root)
application.pack(side="top", fill="both", expand=True)

robot = Robot(application.field.canvas)

def a_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.turn(-5)
	robot.update()

def d_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.turn(5)
	robot.update()

def up_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.linear(0.2)
	robot.update()

def down_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.linear(-0.2)
	robot.update()

def left_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.strafe(-0.2)
	robot.update()

def right_key(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.strafe(0.2)
	robot.update()

def up_ls_pos(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.strafe(0.2)
	robot.update()

def up_ls_neg(event):
	application.set_status("%s: %s", "Keypress", event.keysym)
	robot.strafe(0.2)
	robot.update()

root.bind("a", a_key)
root.bind("d", d_key)
root.bind("<Up>", up_key)
root.bind("<Down>", down_key)
root.bind("<Left>", left_key)
root.bind("<Right>", right_key)

root.mainloop()

