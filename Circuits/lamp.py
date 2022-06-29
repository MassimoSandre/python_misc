import pygame
from object import Object
import math

class Lamp(Object):
    def __init__(self, pos_x, pos_y):
        self.active = False
        self.radius = 20
        Object.__init__(self=self,pos_x=pos_x, pos_y=pos_y, width=20, height=20, passive=True)

    def is_active(self):
        return self.active

    def get_border_width(self):
        if self.active:
            return 0
        else:
            return 2

    def get_position(self):
        return (self.pos_x, self.pos_y)

    def is_inside(self, point_x, point_y):
        d = math.sqrt((self.pos_x - point_x)**2 + (self.pos_y - point_y)**2)
        if d < self.radius:
            return True
        else:
            return False

    def render(self, screen):
        if self.active:
            pygame.draw.circle(screen,(255,0,0), (self.pos_x, self.pos_y),self.radius,0)
        else:
            pygame.draw.circle(screen,(255,255,255), (self.pos_x, self.pos_y),self.radius,2)