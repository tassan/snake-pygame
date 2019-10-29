import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode([640, 480], 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Hello, World!")

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        pygame.display.update()