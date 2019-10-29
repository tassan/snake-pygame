import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake em Python com Pygame")

# Definindo a nossa cobra
snake_positions = [(300, 300), (310, 300), (320, 300)]
snake = pygame.Surface((10, 10))
snake.fill((0, 255, 0))

# Definindo a nossa maçã
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        x = random.randint(0, 630)
        y = random.randint(0, 470)
        screen.blit(apple, (x//10 * 10, y//10 * 10))
        
        for pos in snake_positions:
            screen.blit(snake, pos)

        pygame.display.update()