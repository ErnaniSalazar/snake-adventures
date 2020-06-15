class Vector2(object):
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def add(self, otherVector2):
		x = self.x + otherVector2.x
		y = self.y + otherVector2.y
		return Vector2(x, y)

	def sub(self, otherVector2):
		x = self.x - otherVector2.x
		y = self.y - otherVector2.y
		return Vector2(x, y)

	def multiply(self, number):
		x = self.x * number
		y = self.y * number	
		return Vector2(x, y)

	def equal(self, otherVector2):
		return (self.x == otherVector2.x) and (self.y == otherVector2.y)

	def copy(self):
		return Vector2(self.x ,self.y)

	def toString(self):
		return "x: "+ str(self.x)+ ",y: "+str(self.y) 
