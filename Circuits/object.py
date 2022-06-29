import pygame

class Object():
    def __init__(self, pos_x, pos_y, width, height, passive):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.active = False
        self.passive = passive

    def set_active(self, active):
        self.active = active

    def deactivate_if_passive(self):
        if self.passive:
            self.active = False

    def is_passive(self):
        return self.passive

    def translate(self, comp_x, comp_y):
        self.pos_x += comp_x
        self.pos_y += comp_y

    def is_inside(self, point_x, point_y):
        if point_x < self.pos_x:
            return False
        if point_x > self.pos_x + self.width:
            return False
        if point_y < self.pos_y:
            return False
        if point_y > self.pos_y + self.height:
            return False
        return True

    def get_position(self):
        return (self.pos_x+10, self.pos_y+10)
    
    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def on_leftclick(self):
        pass

    def update(self):
        pass

    def get_border_width(self):
        return 2

    def render(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.get_rect(), self.get_border_width())
