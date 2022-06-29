import pygame
import random
from pygame.locals import *
from Fourier_series import Fourier_series


size = width, height = 620, 540

black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()

running = True

NUM = 10

MUL = 1

cur = Fourier_series(50,NUM, MUL)
for i in range (0,NUM-1):
    fr = Fourier_series(50, (NUM-1-i),MUL)
    fr.append(cur)
    cur = fr


theta = 0
print(cur.next)


while running:
    screen.fill(black)


    cur.render(screen,(width//2, height//2),theta)
    theta+=0.01

    pygame.display.update()
    clock.tick(60)