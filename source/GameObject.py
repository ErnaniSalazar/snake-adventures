import pygame
class GameObject(object):
	def __init__(self, pos, size, color):
		self.pos=pos
		self.size=size
		self.color=color
		self.sprite=None
	def draw(self):
		pass

	def move(self, direction, amount):
		self.sprite.move(direction.x*amount, direction.y*amount)