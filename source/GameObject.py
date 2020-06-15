import pygame
from Vector2 import Vector2
class GameObject(object):
	def __init__(self, scene, pos, size, color):
		self.scene = scene
		self.pos=pos
		self.size=size
		self.color=color
		self.sprite=None
		
	def draw(self):
		pass

	def move(self, direction, amount):
		directionAux = direction.multiply(amount)
		self.pos = self.pos.add(directionAux)
    
	def getType(self):
		pass   

	def disappear(self):
		pass
		