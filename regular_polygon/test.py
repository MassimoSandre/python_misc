import pygame
import random
from pygame.locals import *
from regular_polygons import *


size = width, height = 800, 800

black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()

running = True


# i = 3
# tick = 0

hx = Ennagram((400,400),390,0)

while running:
    screen.fill(black)

    
    pygame.draw.polygon(screen, (255,255,255),hx.get_points(), width=1)
    #hx.rotate(0.1)
    # if tick == 10:
    #     tick = 0
    #     i+=1
    # else:
    #     tick+=1
    # if i > 20:
    #     i = 3

    pygame.display.update()
    clock.tick(60)