import pygame
from GameObject import GameObject
from Vector2 import Vector2
from Bullet import Bullet
from Food import Food

class SnakePart(GameObject):
	def __init__(self, scene, lastOrientation, direction, pos, size, color):
		super().__init__(scene, pos, size, color)
		self.lastOrientation = lastOrientation
		self.direction = direction
		self.sprite = pygame.Rect(pos.x, pos.y, size.x, size.y)

	def draw(self, screen):
		self.sprite.top = self.pos.y
		self.sprite.left = self.pos.x
		pygame.draw.rect(screen, self.color, self.sprite)
		
	def movePart(self, direction, amount):		
		self.lastOrientation = self.direction
		self.direction = direction
		self.move(direction, amount)

	def getType(self):
		return "SnakePart"

	
class Snake(GameObject):
	def __init__(self, scene, pos, size, color):
		super().__init__(scene, pos, size, color)
		self.bodyParts=[SnakePart(self.scene, Vector2(0, 0), Vector2(0, 0), pos, size, self.color)]
	def eat(self):
		headPosition = self.getLast().pos
		headDirection = self.getLast().direction
		newDirection = headDirection.multiply(30)
		newPosition = headPosition.sub(newDirection)
		self.bodyParts.append(SnakePart(self.scene, Vector2(0, 0), Vector2(0, 0), newPosition, self.size, self.color))
	def colorChange(self, r, g, b):
		newColor = pygame.Color(r, g, b)
		for bodyPart in self.bodyParts:
			bodyPart.color = newColor
		self.color = newColor	
	def openFire(self):
		if len(self.bodyParts) == 1:
			return		
		arrowPos = self.getHead().pos.add(self.getHead().direction.multiply(35))
		placeHolder = Food(self.scene, arrowPos, 0, Vector2(0, 0), pygame.Color(255, 255, 255), None)
		arrowPosition = self.getHead().pos.copy().add(self.getHead().direction.multiply(30))
		self.bodyParts.pop()
		arrow = Bullet(self.scene, arrowPosition, 0, Vector2(10, 10), pygame.Color(0, 255, 255),
			placeHolder, atk = 1, hp = 1, speed = 30)
		self.scene.objects["worldGameObjects"].append(arrow)
	def dropTheBomb(self):
		if len(self.bodyParts) == 1:
			return		
		minePosition = self.getHead().pos.copy().add(self.getHead().direction.multiply(-30))
		self.bodyParts.pop()
		bomb = Bullet(self.scene, minePosition, 0, Vector2(25, 25), pygame.Color(0, 200, 255),
			None, atk = 5, hp = 2, speed = 30)
		self.scene.objects["worldGameObjects"].append(bomb)
	def moveSnake(self, direction, amount):
		lastBodyPart = None
		
		for i in range(0, len(self.bodyParts)):
			currBodyPart=self.bodyParts[i]
			if i==0:
				currBodyPart.movePart(direction, 30)

			else:
				currBodyPart.movePart(lastBodyPart.lastOrientation, 30)
				
			lastBodyPart = currBodyPart

	def draw(self, screen):
		for currBodyPart in self.bodyParts:
			currBodyPart.draw(screen)
	def getHead(self):
		return self.bodyParts[0]

	def getLast(self):
		return self.bodyParts[-1]
    
	def getType(self):
		return "Snake"
	def act(self):
		pass




