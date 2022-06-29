from random import randint, random, randrange
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock
from src.particle import Particle
pygame.init()
pygame.font.init()
SIZE = WIDTH, HEIGHT = (600,400)
BGCOLOR = (50,50,50)
GFONT = pygame.font.SysFont("Comic Sans MS", 30)
window = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
pygame.display.set_caption('Particles')
clock = Clock()

particles = [Particle(pygame.Vector2(int(randint(0,WIDTH)),int(randint(0,HEIGHT))), 2, randrange(0,6)) for i in range(50)]

def main():
    
    running = True
    current_size = SIZE
    while running:
        clock.tick(60)
        sus_size = window.get_rect()
        
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        window.fill(BGCOLOR)


        for sus in particles:
            sus.update(window.get_rect())
            sus.show(window)
            sus.velocity = (window.get_height()  +  window.get_width()) // 500
            
        for i in range(0,len(particles)):
            for j in range(i+1, len(particles)):
                particles[i].show_arc(window, particles[j])


        pygame.display.update()

if __name__ == '__main__':
    main()