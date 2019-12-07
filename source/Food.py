import pygame
from GameObject import GameObject
class Food(GameObject):
	def __init__(self, pos, score, size, color, atk= 0, hp=1):
		super(). __init__(pos, size, color) #call father constructor
		self.score=score
		self.hp=hp
		self.atk=atk

		self.sprite = pygame.Rect(pos.x,pos.y,size.x, size.y)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.sprite)





	 
