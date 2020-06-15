import pygame
from GameObject import GameObject
class WallE(GameObject):
	def __init__(self, pos, size, color):
		super(). __init__(pos, size, color) 


		self.sprite = pygame.Rect(pos.x,pos.y,size.x, size.y)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.sprite)

	def getType(self):
		return "WallE"



	 
