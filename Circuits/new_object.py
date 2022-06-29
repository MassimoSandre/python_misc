from menu_voice import Menu_voice
from switch import Switch
from lamp import Lamp

class New_object(Menu_voice):
    def __init__(self, value, linked_object):
        self.linked_object = linked_object
        Menu_voice.__init__(self=self, value=value)

    def create(self):
        if self.linked_object == "switch":
            return Switch(0,0)
        elif self.linked_object == "lamp":
            return Lamp(0,0)