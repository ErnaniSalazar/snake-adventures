import pygame
from GameObject import GameObject
from Vector2 import Vector2

class Text(GameObject):
	def __init__(self, scene, pos, size, color, fontPath, text, antialias = False, background = None):
		super(). __init__(scene, pos, size, color) 
		self.font = pygame.font.Font(fontPath, size.x)
		self.antialias =antialias
		self.background = background
		self.text=text

	def setText(self, text):
		self.text = text

	def draw(self, screen):
		textDisplay = self.font.render(self.text, self.antialias, self.color, self.background)
		screen.blit(textDisplay, (self.pos.x, self.pos.y))

	def act(self):
		pass
		
	def getType(self):
		return "Text"



	 
