from object import Object

class Gate(Object):
    def __init__(self, pos_x, pos_y):
        Object.__init__(self=self, pos_x=pos_x, pos_y=pos_y, width=30, height=30, passive=boh)

    def update(self):
        pass