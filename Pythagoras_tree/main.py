import pygame
from tree import Tree

pygame.init()

size = width, height = (600,600)
bgcolor = (30,30,30)

window = pygame.display.set_mode(size)
pygame.display.set_caption('Pythagoras Tree')
clock = pygame.time.Clock()
window.fill(bgcolor)


tree = Tree(pos=(275,550), leng=50, base_angle=0, rot_angle=45, screen=window)

tree.draw(-1)

while True:
    clock.tick(60)
    