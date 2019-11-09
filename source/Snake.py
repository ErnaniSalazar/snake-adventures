 

class SnakePart(GameObject):
	def __init__(lastOrientation, posInGrid, size, color, sprite=None)
		self.lastOrientation=lastOrientation
		super().__init__(posInGrid, size, color, sprite)



class Snake(object):
	def __init__(self, size, color, sprite=None):
		self.size=size
		self.color=color
		self.sprite=sprite

		self.bodyParts=[SnakePart(0, posInGrid, size, color)]

		def move(direction, amount):
			for i in range(0, len(self.bodyParts)):
				currBodyPart=self.bodyParts[i]
				if i==0:
					currBodyPart.move(direction, amount)
					currBodyPart.lastOrientation=direction
				else:
					currBodyPart.move(lastOrientation, amount)
