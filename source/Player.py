from Vector2 import Vector2
from Snake import Snake
from Snake import SnakePart
import pygame
class Player(object):
    def __init__(self, snake, score, currDirection, atk=1, hp=3):
        self.snake=snake
        self.score=score
        self.currDirection=currDirection
        self.hp=hp
        self.atk=atk
        self.amount = 30
        self.hasShield = False

    def handleKeys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.currDirection = Vector2(-1, 0)
        if key[pygame.K_RIGHT]:
            self.currDirection = Vector2(1, 0)
        if key[pygame.K_UP]:
            self.currDirection = Vector2(0, -1)
        if key[pygame.K_DOWN]:
            self.currDirection = Vector2(0, 1)
        if key[pygame.K_f]:
            self.snake.openFire()
        if key[pygame.K_d]:
            self.snake.dropTheBomb()
        if key[pygame.K_s]:
            self.raiseShield()
        if key[pygame.K_g]:
            self.heal()

    def raiseShield(self):
        if self.hasShield:
            self.hasShield=False
            self.snake.colorChange(200, 0, 0)
            return
        if len(self.snake.bodyParts) == 1:
            return
        self.hasShield = True
        self.snake.colorChange(200, 200, 200)
        
    def getHit(self, amount):
        if self.hasShield:
            self.snake.colorChange(200, 0, 0)
            self.snake.bodyParts.pop()
        else:
            self.hp = self.hp - amount
    
    def heal(self):
        if len(self.snake.bodyParts) == 1 or self.hasShield or self.hp == 10:
            return
        else:
            self.hp = self.hp + 3
            self.snake.bodyParts.pop()
            if self.hp >= 10:
                self.hp = 10
                
    def draw(self, screen):
        self.snake.draw(screen)

    def act(self):
        if self.hasShield:
            return
        self.snake.moveSnake(self.currDirection, self.amount)

    def getType(self):
        return "Player"