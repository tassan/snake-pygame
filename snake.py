import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake em Python com Pygame")

# Definindo a nossa cobra
snake_pos = [(300, 300), (310, 300), (320, 300)]
snake = pygame.Surface((10, 10))
snake.fill((0, 255, 0))


def posicao_aleatoria():
    x = random.randint(0, 630)
    y = random.randint(0, 470)
    return (x//10 * 10, y//10 * 10)


# Definindo a nossa maçã
apple_position = posicao_aleatoria()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))


def direcao():
    direcao = 0
    
    if event.type == KEYDOWN:
        if event.key == K_UP:
            direcao = 0
        if event.key == K_DOWN:
            direcao = 2
        if event.key == K_RIGHT:
            direcao = 1
        if event.key == K_LEFT:
            direcao = 3
    
    return direcao


running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    direcao_cobra = direcao()

    for i in range(len(snake_pos) - 1, 0, -1):
        snake_pos[i] = (snake_pos[i-1][0], snake_pos[i-1][1])
    
    screen.blit(apple, apple_position)
    for pos in snake_pos:
        screen.blit(snake, pos)

    pygame.display.update()