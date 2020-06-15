import pygame
import random
from Vector2 import Vector2
from GameObject import GameObject

class Food(GameObject):
	def __init__(self, scene, pos, score, size, color, target, atk= 0, hp=1, speed=0):
		super(). __init__(scene, pos, size, color) 
		self.score=score
		self.hp=hp
		self.atk=atk
		self.speed = speed
		self.initialHP = hp
		self.sprite = pygame.Rect(pos.x,pos.y,size.x, size.y)
		self.lastDirection = Vector2(0, 0)
		self.target = target
	def getHit(self, amount):
		self.hp = self.hp - amount
	def pursuit(self):
		if self.target == None:
			return Vector2(0, 0)
		directionAux = Vector2(0, 0)
		if self.pos.x < self.target.pos.x :
			directionAux.x = 1
		elif self.pos.x > self.target.pos.x :
			directionAux.x = -1

		if self.pos.y < self.target.pos.y :
			directionAux.y = 1
		elif self.pos.y > self.target.pos.y :
			directionAux.y = -1
		return directionAux
	def draw(self, screen):
		self.sprite.top = self.pos.y
		self.sprite.left = self.pos.x
		pygame.draw.rect(screen, self.color, self.sprite)
	def act(self):
		pass	
	def getType(self):
		return "Food"

