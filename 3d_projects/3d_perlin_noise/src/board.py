from pygame import Vector3
from perlin_noise import PerlinNoise
import pygame
import math

class Board:
    def __init__(self, dim, base_pos, noise_range, point_distance) -> None:
        self.dim = dim
        self.base_pos = Vector3(base_pos)

        self.range = noise_range
        self.point_distance = point_distance

        self.color = (255,255,255)

        self.board = [[0 for _ in range(dim[1])]for _ in range(dim[0])]

    def __map_range(self,value, start1, stop1, start2, stop2):
        return (value - start1) // (stop1 - start1) * (stop2 - start2) + start2

    def update(self):
        biugos = PerlinNoise()

        yoff = 0
        for y in range(self.dim[0]):
            xoff = 0
            for x in range(self.dim[1]):
                #print(biugos([float(xoff), float(yoff)]))
                self.board[x][y] = self.__map_range(biugos([float(xoff), float(yoff)]),-1,1,self.range[0],self.range[1])
                xoff += 0.1
            yoff +=0.1

    def __project_z(self,vec):
        base = [Vector3(1,0,0), Vector3(0,1,0)]

        result = Vector3(0,0,0)
        for b in base:
            p = Vector3.dot(vec, b)
            result = result+ (p*b)
    
        return result

    def __matrix_vector_product(self,mat, vec):
        result = []
        for line in mat:
            result.append(Vector3.dot(Vector3(line), vec))

        return Vector3(result)

    def __rotate_x(self,vec, theta):
        mat = [(1, 0,0), (0, math.cos(theta), -math.sin(theta)), (0, math.sin(theta), math.cos(theta))]

        return self.__matrix_vector_product(mat, vec)

    def show(self, screen):
        
        for i in range(self.dim[0]):
            #s = []
            for j in range(self.dim[1]):
                x = i*self.point_distance
                y = self.board[i][j]
                z = j*self.point_distance

                #s.append(self.__project_z(Vector3(x,y,z) + self.base_pos))   

                pygame.draw.circle(screen,self.color,self.__project_z(self.__rotate_x(Vector3(x,y,z) + self.base_pos,  +0.8))[:2],3)
            #print(s)

        
        #quit()
                




