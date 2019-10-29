import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode([640, 480], 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Hello, World!")

# Definindo a nossa maçã
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(apple, (30, 40))

        pygame.display.update()