import pygame
import random
from Vector2 import Vector2
from GameObject import GameObject
from Food import Food
from Bullet import Bullet

class Enemy(Food):
	def __init__(self, scene, pos, score, size, color, target, atk= 1, hp=2, speed=30):
		super(). __init__(scene, pos, score, size, color, target, atk, hp, speed) 
		self.bullets = []
	
	def moveRandom(self):
		return random.choice([Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)])
	def move(self):
		randomNumber = random.randint(0, 5)
		if randomNumber == 0:
			directionAux = self.pursuit()
		else:
			directionAux = self.moveRandom()
		directionAux = directionAux.multiply(self.speed)
		self.pos = self.pos.add(directionAux)
		self.lastDirection = directionAux
		
	
	def retreat(self):
		self.lastDirection = self.lastDirection.multiply(-1)
		self.pos = self.pos.add(self.lastDirection)

	def openFire(self):
		bullet = Bullet(self.scene, self.pos.copy(), 0, Vector2(10, 10), pygame.Color(0, 0, 255), self.target, atk = 1, hp = 1, speed = 30)
		self.scene.objects["worldGameObjects"].append(bullet)
	def act(self):
		randomNumber = random.randint(0, 6)
		if randomNumber == 0:
			self.openFire()
		else:
			self.move()
	
	def draw(self, screen):
		self.sprite.top = self.pos.y
		self.sprite.left = self.pos.x
		pygame.draw.rect(screen, self.color, self.sprite)
		for bullet in self.bullets :
			bullet.draw(screen)
	def getType(self):
		return "Enemy"

