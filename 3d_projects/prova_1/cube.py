import utils
import pygame 

class Cube():
    def __init__(self, pos=(0,0,0), dim=(10,10,10)) -> None:
        self.pos = pos
        self.vectors = [(dim[0],0,0), (0,dim[1],0), (0,0,dim[2])]

        self.tri_comps = [(0,1,2), (1,2,3), (0,2,4),(2,4,6), (0,1,4), (1,4,5), (2,3,6), (3,6,7), (4,5,6), (5,6,7), (1,3,5), (3,5,7)]

    def set_pos(self, pos):
        self.pos = pos

    def rotate_x(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_x(self.vectors[i], theta)

    def rotate_y(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_y(self.vectors[i], theta)

    def rotate_z(self, theta) -> None:
        for i in range(len(self.vectors)):
            self.vectors[i] = utils.rotate_z(self.vectors[i], theta)

    def render(self,window):
        vertex3d = []
        for v1 in range(2):
            for v2 in range(2):
                for v3 in range(2):
                    vertex3d.append(utils.vector_sum(self.pos, utils.k_vector(self.vectors[0],v1), utils.k_vector(self.vectors[1],v2), utils.k_vector(self.vectors[2],v3)))

        vertex2d = []
        for v3 in vertex3d:
            vertex2d.append(utils.project_z(v3)[:2])

        #print(vertex3d)

        for tri in self.tri_comps:
            cur_tri = []
            for comp in tri:
                cur_tri.append(vertex2d[comp])
            pygame.draw.polygon(window, (255,255,255), cur_tri, 1)