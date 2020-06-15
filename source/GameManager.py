# Import and initialize the pygame library
import pygame
import pdb
import random
import math
import os
import sys
from WallE import WallE
from Snake import Snake
from Snake import SnakePart
from Player import Player
from Food import Food
from Vector2 import Vector2
from Text import Text
from Enemy import Enemy
from Bullet import Bullet
from GameGlobals import SceneManager
from Scene import Scene

pygame.init()

pygame.display.set_caption("Snake Adventures Beta 3.1.0")
screen = pygame.display.set_mode([720, 720])
sceneManager = SceneManager(screen)
sceneManager.initScenes()
sceneManager.sceneLoad(sceneManager.homeScene)
screen.fill((0,0,0))
running = True	
while running:
	screen.fill((0, 0, 0))
	sceneManager.currScene.update()
	
    # Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	pygame.display.flip()
	pygame.display.update()
pygame.quit()