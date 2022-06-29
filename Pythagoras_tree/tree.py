import pygame
import math

class Tree:
    def __init__(self, pos, leng, base_angle, rot_angle, screen) -> None:
        self.pos = pos
        self.leng = leng
        self.base_angle = base_angle
        self.rot_angle = rot_angle
        self.screen = screen

    def __draw(self, pos, leng, cur_angle, max_depth):
        if max_depth == 0 or leng < 2:
            return

        tx,ty = p1 = pos
        
        p2 = tx + leng*math.cos(math.radians(cur_angle)), ty - leng*math.sin(math.radians(cur_angle))
        p4 = tx + leng*math.cos(math.radians(cur_angle+90)), ty - leng*math.sin(math.radians(cur_angle+90))
        tx,ty = p4
        p3 = tx + leng*math.cos(math.radians(cur_angle)), ty - leng*math.sin(math.radians(cur_angle))

        pygame.draw.polygon(self.screen, (255,255,255), (p1,p2,p3,p4), 0)


        pygame.display.update()

        self.__draw(p4,leng*math.cos(math.radians(self.rot_angle)),cur_angle+self.rot_angle,max_depth-1)

        np = tx + leng*math.cos(math.radians(cur_angle+self.rot_angle))*math.cos(math.radians(self.rot_angle)), ty - leng*math.sin(math.radians(cur_angle+self.rot_angle))*math.cos(math.radians(self.rot_angle))

        self.__draw(np, leng*math.sin(math.radians(self.rot_angle)), cur_angle-90+self.rot_angle, max_depth-1)

        



    def draw(self, max_depth):
        self.__draw(self.pos, self.leng, self.base_angle, max_depth)



    
