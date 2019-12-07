from Vector2 import Vector2
import pygame
class Player(object):
    def __init__(self, snake, score, atk=1, hp=3):
        self.snake=snake
        self.score=score
        self.hp=hp
        self.atk=atk


    def handleKeys(self):
        key = pygame.key.get_pressed()
        amount = 200
        if key[pygame.K_LEFT]:
            print("aaaa")
            self.snake.move(Vector2(-1, 0), amount)
        if key[pygame.K_RIGHT]:
            self.snake.move(Vector2(1, 0), amount)
        if key[pygame.K_UP]:
            self.snake.move(Vector2(0, 1), amount)
        if key[pygame.K_DOWN]:
            self.snake.move(Vector2(0, -1), amount)

    def draw(self, screen):
        self.snake.draw(screen)
