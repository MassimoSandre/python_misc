import imp
from msilib.schema import Directory
from random import randint
from pygame import Vector3
from math import dist
import math
import pygame
from pygame import gfxdraw
import colorsys

class Particle:
    def __init__(self,position,velocity,direction) -> None:

        self.position:Vector3 = position
        self.velocity:int = velocity
        self.direction:Vector3 = Vector3(direction)
        self.direction = self.direction.normalize()

        self.color:tuple = (50,50,50)
        self.SIZE:int = 8
        self.MIN_DIST_CONNECT = 250
        self.FADING_DISTANCE = 100
        self.Z_RANGE = (-60,200)

    def __project_z(self,vec):
        base = [Vector3(1,0,0), Vector3(0,1,0)]

        result = Vector3(0,0,0)
        for b in base:
            p = Vector3.dot(vec, b)
            result = result+ (p*b)
    
        return result
    
    def update(self, borders):
        new_pos = Vector3(self.position[0]+self.direction[0]*self.velocity, self.position[1]+self.direction[1]*self.velocity, self.position[2]+self.direction[2]*self.velocity)
        
        projected_pos = self.__project_z(new_pos)
        
        if not borders.collidepoint(projected_pos[:2]) or new_pos.z<self.Z_RANGE[0] or new_pos.z > self.Z_RANGE[1]:
            self.direction = -self.direction # Vorrei ricordare che Davide Prandini ti ha etichettato come "pazzo" per aver imparato [molte] cifre del pigreco
        else:
            self.position = new_pos
    
    
    def show(self, window) -> None:
        pygame.draw.circle(window,self.color,self.__project_z(self.position)[:2],self.SIZE - (self.position.z/100)*(self.SIZE/1.5))
        #print(self.__project_z(self.position)[:2])
    
    def map_range(self,value, start1, stop1, start2, stop2):
        return (value - start1) // (stop1 - start1) * (stop2 - start2) + start2
    
    def show_arc(self, window, particle_to_connect):
        if particle_to_connect == self:
            return
        d = dist(particle_to_connect.position, self.position)
        if d >= self.MIN_DIST_CONNECT:
            return

        fading = max(0,d-(self.MIN_DIST_CONNECT-self.FADING_DISTANCE))*(255/self.FADING_DISTANCE)
        
        pos1 = self.__project_z(self.position)
        pos2 = self.__project_z(particle_to_connect.position)

        gfxdraw.line(window,int(pos1.x),int(pos1.y),int(pos2.x),int(pos2.y),(255,255,255,255-int(fading)))
        #gfxdraw.filled_circle(window, int(self.position.x), int(self.position.y), self.SIZE,(255,100,100))
        #print( )