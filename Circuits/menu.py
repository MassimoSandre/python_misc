from object import Object
import pygame

class Menu():
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.width = 150
        self.voices_height = 40
        self.menu_voices = []
        self.visible = False

    def on_leftclick(self, pos_x, pos_y):
        if pos_x < self.pos_x:
            return None
        if pos_x > self.pos_x + self.width:
            return None
    
        if pos_y < self.pos_y:
            return None

        
        if pos_y > self.pos_y + self.voices_height*len(self.menu_voices):
            return None
        
        x = self.menu_voices[int((pos_y-self.pos_y)/self.voices_height)].create()
        x.set_position(self.pos_x, self.pos_y)
        return x

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        

    def add_voice(self, voice):
        self.menu_voices.append(voice)

    def is_displayed(self):
        return self.visible

    def render(self, screen):
        if self.visible:
            #print(self.pos_x)
            pygame.draw.rect(screen, (255,0,0), pygame.Rect((self.pos_x, self.pos_y),(self.width, self.voices_height*len(self.menu_voices))), 0)

    def display(self):
        self.visible = True

    def hide(self):
        self.visible = False