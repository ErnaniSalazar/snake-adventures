import pygame
import random
from Vector2 import Vector2
from GameObject import GameObject
from Food import Food
class Bullet(Food):
	def __init__(self, scene, pos, score, size, color, target, atk= 0, hp=1, speed=0):
		super(). __init__(scene, pos, score, size, color, target, atk, hp, speed) 
		self.direction = self.pursuit()
	def act(self):
		directionAux = self.direction.multiply(self.speed)
		self.pos = self.pos.add(directionAux)

		
	def getType(self):
		return "Bullet"

		
