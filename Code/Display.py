import Tkinter as tk

# Information displayed at bottom of application
class Statusbar(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.label = tk.Label(self, bd=1, relief="sunken", anchor="w")
		self.label.pack(fill="x")

	def set(self, format, *args):
		self.label.config(text=format % args)
		self.label.update_idletasks()

# Graphics for field and robot
class Field(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.canvas = tk.Canvas(self, bg="white", height=1000, width=1000)
		self.canvas.pack()

# Main application
class Display(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.statusbar = Statusbar(parent)
		self.field = Field(parent)

		self.statusbar.pack(side="bottom", fill="x")
		self.field.pack(side="top", fill="x")

	def set_status(self, format, *args):
		self.statusbar.set(format, *args)
