
class Player(object):
    def __init__(self, ident, pos):
        # Player's ID ingame, between 1 to 4
        self.id = ident
        self.pos = pos
    def update(self):
        pass
    def draw(self):
        pass

    def moveUp(self):
        self.pos = (self.pos[0], self.pos[1] - 1)
    def moveDown(self):
        self.pos = (self.pos[0], self.pos[1] + 1)
    def moveLeft(self):
        self.pos = (self.pos[0] - 1, self.pos[1])
    def moveRight(self):
        self.pos = (self.pos[0] + 1, self.pos[1])
