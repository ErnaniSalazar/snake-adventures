import pygame
from GameObject import GameObject
class SnakePart(GameObject):
	def __init__(self, lastOrientation, pos, size, color, sprite):
		super().__init__(pos, size, color)
		self.lastOrientation = lastOrientation
		self.sprite = sprite

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.sprite)

	


class Snake(object):
	def __init__(self, pos, size, color):
		self.size=size
		self.color=color

		self.bodyParts=[SnakePart(0, pos, size, color, pygame.Rect(pos.x, pos.y, size.x, size.y))]

	def move(self, direction, amount):
		for i in range(0, len(self.bodyParts)):
			currBodyPart=self.bodyParts[i]
			if i==0:
				currBodyPart.move(direction, amount)
				currBodyPart.lastOrientation = direction
			else:
				currBodyPart.move(lastOrientation, amount)

	def draw(self, screen):
		for currBodyPart in self.bodyParts:
			currBodyPart.draw(screen)