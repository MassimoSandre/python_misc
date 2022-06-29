import math

class Regular_polygon:
    def __init__(self, sides:int, pos=(0,0),radius:int=0, rotation_rad:float=0) -> None:
        if sides < 3:
            raise Exception("'sides' must be 3 or greater")
        
        self.pos = pos
        self.sides = sides
        self.radius = radius
        self.rotation = rotation_rad

    def get_points(self):
        points = []
        for i in range(self.sides):
            dx = int(self.radius*math.cos(2*math.pi/self.sides*i+self.rotation))
            dy = -int(self.radius*math.sin(2*math.pi/self.sides*i+self.rotation))

            points.append((self.pos[0]+dx,self.pos[1]+dy))
        return points


    def set_rotation(self, rotation_rad):
        self.rotation = rotation_rad
    
    def rotate(self, rotation_rad):
        self.rotation += rotation_rad

    def scale(self, multiplier):
        self.radius = int(self.radius*multiplier)

    def set_radius(self, radius):
        self.radius = radius

    def translate(self, vector):
        self.pos[0]+=vector[0]
        self.pos[1]+=vector[1]

    def set_pos(self, pos):
        self.pos = pos


class Triangle(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(3, pos, radius, rotation_rad+math.pi/2)

class Square(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(4, pos, radius, rotation_rad+math.pi/4)

class Pentagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(5, pos, radius, rotation_rad)

class Hexagon(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(6, pos, radius, rotation_rad)

class Heptagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(7, pos, radius, rotation_rad)

class Octagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(8, pos, radius, rotation_rad)

class Ennagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(9, pos, radius, rotation_rad)

class Decagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(10, pos, radius, rotation_rad)

class Hendecagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(11, pos, radius, rotation_rad)

class Dodecagram(Regular_polygon):
    def __init__(self, pos=(0, 0), radius: int = 0, rotation_rad: float = 0) -> None:
        super().__init__(12, pos, radius, rotation_rad)
