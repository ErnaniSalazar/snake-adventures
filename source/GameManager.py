# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import math
import os
import sys

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Snake 2D prototype 1.0.0")

class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(350, 350, 14, 14))

    def handle_keys(self):
         key = pygame.key.get_pressed()
         dist = 1
         if key[pygame.K_LEFT]:
             self.rect.move(-1, 0)  
         if key[pygame.K_RIGHT]:
             self.rect.move(1, 0)          
         if key[pygame.K_UP]:
             self.rect.move(0, 1)
         if key[pygame.K_DOWN]:
             self.rect.move(0, -1)
           
    def draw(self, surface):
         pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(350, 350, 14, 14))

class Points(object):
    def __init__(self):
        self.circle = pygame.draw.circle(screen, (200, 200, 200), (random.randint(15, 685), random.randint(15, 685)), 7)

    def draw(self):
        pygame.draw.circle(screen, (200, 200, 200), (random.randint(15, 685), random.randint(15, 685)), 7)

screen.fill((0,0,0))

player = Player()

points = Points()

snakelength = 1
print("score:")



# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    player.draw(screen)

    player.handle_keys()

    points.draw()

    pygame.time.wait(100)
   
    pygame.display.flip()
pygame.quit()