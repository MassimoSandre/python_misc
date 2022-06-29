from tokenize import Hexnumber
from turtle import width
from pendulum import Pendulum
import pygame

SIZE = WIDTH, HEIGHT = 500,500
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

p = Pendulum(5)

scale_x = lambda x: int(x*(WIDTH/2/p.n))
scale_y = lambda y: int(-y*(HEIGHT/2/p.n))

running = True

while running:
    screen.fill([0,0,0])

    coords = p.get_coordinates()

    x1,y1 = WIDTH//2, HEIGHT//2

    for i in range(p.n):
        x2,y2 = WIDTH//2 + scale_x(coords[i][0]), HEIGHT//2 + scale_y(coords[i][1])

        pygame.draw.line(screen, [255,255,255], (x1,y1), (x2,y2), 1)
        pygame.draw.circle(screen, (255,0,0), (x1,y1), 4,0)

        x1,y1 = x2,y2

    
    p.update(1/60)

    pygame.display.update()
    clock.tick(10)
    