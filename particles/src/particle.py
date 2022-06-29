import imp
from random import randint
from pygame import Vector2
from math import dist
import math
import pygame
from pygame import gfxdraw
import colorsys


class Particle:

    def __init__(self,position,velocity,direction) -> None:

        self.position:Vector2 = position
        self.velocity:int = velocity
        self.direction = direction

        self.color:tuple = (50,50,50)
        self.SIZE:int = 3
        self.MIN_DIST_CONNECT = 100
        self.FADING_DISTANCE = 20

    
    def update(self, borders):
        dx = math.cos(self.direction)*self.velocity
        dy = math.sin(self.direction)*self.velocity
        
        new_pos = Vector2(self.position[0]+dx, self.position[1]+dy)
        
        
        if not borders.collidepoint(new_pos):
            self.direction = self.direction-3.1415926 + randint(-1,1)/3# Vorrei ricordare che Davide Prandini ti ha etichettato come "pazzo" per aver imparato [molte] cifre del pigreco
        else:
            self.position = new_pos
    
    
    def show(self, window) -> None:
        pygame.draw.circle(window,self.color,self.position,self.SIZE)
    
    def map_range(self,value, start1, stop1, start2, stop2):
        return (value - start1) // (stop1 - start1) * (stop2 - start2) + start2
    
    def show_arc(self, window, particle_to_connect):
        if particle_to_connect == self:
            return
        d = dist(particle_to_connect.position, self.position)
        if d >= self.MIN_DIST_CONNECT:
            return

        fading = max(0,d-(self.MIN_DIST_CONNECT-self.FADING_DISTANCE))*(255/self.FADING_DISTANCE)
        
        gfxdraw.line(window,int(self.position.x),int(self.position.y),int(particle_to_connect.position.x),int(particle_to_connect.position.y),(255,255,255,255-int(fading)))
        gfxdraw.filled_circle(window, int(self.position.x), int(self.position.y), self.SIZE,(255,100,100))
        print( )