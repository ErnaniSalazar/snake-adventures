import pygame
from GameObject import GameObject
from Food import Food
class WallE(Food):
	def __init__(self, scene, pos, size, color):
		super().__init__(scene, pos, 0, size, color, None, 999, 999, 0)

		self.sprite = pygame.Rect(pos.x,pos.y,size.x, size.y)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.sprite)

	def act(self):
		pass

	def getType(self):
		return "WallE"



	 
