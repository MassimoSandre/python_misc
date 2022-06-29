import pygame

class Wire():
    def __init__(self, ob1, ob2):
        self.ob1 = ob1
        self.ob2 = ob2
        self.status = False

    def render(self, screen):
        pygame.draw.line(screen, (255,255,255), self.ob1.get_position(), self.ob2.get_position())

    def update(self):
        self.status = False

        #print(self.ob1.is_active())
        #print(self.ob1.is_passive())

        if self.ob1.is_active() and not self.ob1.is_passive():
            self.status = True
        if self.ob2.is_active() and not self.ob2.is_passive():
            self.status = True

        if self.status:
            if self.ob1.is_passive():
                self.ob1.set_active(True)

            if self.ob2.is_passive():
                self.ob2.set_active(True)

