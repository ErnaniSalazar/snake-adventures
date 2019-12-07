# Import and initialize the pygame library
import pygame
import random
import math
import os
import sys

from Snake import Snake
from Player import Player
from Food import Food
from Vector2 import Vector2


pygame.init()

pygame.display.set_caption("Snake 2D prototype 1.9.0")

screen = pygame.display.set_mode([700, 700])
screen.fill((0,0,0))

snake = Snake(Vector2(335, 365), Vector2(30, 30), pygame.Color(200, 0, 0))
player = Player(snake, 0, atk=1, hp=3)
food = Food(Vector2(245, 456), 1, Vector2(30, 30), pygame.Color(0, 247, 0), hp=1)
enemy = Food(Vector2(344, 345), 1, Vector2(30, 30), pygame.Color(100, 0, 100), atk=1, hp=1)
gameObjects = [player, food, enemy]


# Run until the user asks to quit
running = True
while running:
	player.handleKeys()

	for gameObject in gameObjects:
		gameObject.draw(screen)




    # Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

	player.draw(screen)


	

	pygame.time.wait(4)
pygame.quit()