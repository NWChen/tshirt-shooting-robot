from Tkinter import *


def foo():
	print "bar"
root = Tk()

root.bind("<Visibility>", foo())
root.mainloop()