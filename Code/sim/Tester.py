
def get_wheel_angle(wheel):
	center = wheel.center
	diagonal_length = radius/4
	self.corners = [Point(center.x-diagonal_length/math.sqrt(5), center.y+2*diagonal_length/math.sqrt(5)),
								Point(center.x+diagonal_length/math.sqrt(5), center.y+2*diagonal_length/math.sqrt(5)),
								Point(center.x-diagonal_length/math.sqrt(5), center.y-2*diagonal_length/math.sqrt(5)),
								Point(center.x+diagonal_length/math.sqrt(5), center.y-2*diagonal_length/math.sqrt(5))]