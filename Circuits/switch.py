from object import Object

class Switch(Object):
    def __init__(self, pos_x, pos_y):
        self.active = False
        Object.__init__(self=self,pos_x=pos_x, pos_y=pos_y, width=20, height=20, passive=False)

    def on_leftclick(self):
        self.active = not self.active

    def is_active(self):
        return self.active

    def get_border_width(self):
        if self.active:
            return 0
        else:
            return 2