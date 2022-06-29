import pygame
import math

class Fourier_series:
    def __init__(self, arg1, arg2, mul=100) -> None:
        self.arg1 = arg1
        self.arg2 = arg2

        self.mul = mul

        self.next = None

    def append(self, next_fr):
        self.next = next_fr

    def render(self, screen, pos, theta):
        dx = int(self.mul*self.arg1*math.sin(self.arg2*theta))
        dy = -int(self.mul*self.arg1*math.cos(self.arg2*theta))

        ending = (pos[0]+dx, pos[1]+dy)

        pygame.draw.line(screen, (255,255,255), pos, ending)
        if self.next != None:
            self.next.render(screen, ending, theta)
