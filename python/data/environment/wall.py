# Might null the Wall object and just make a list of walls
class Wall(EnvironmentObject):
    def __init__(self, pos):
        self.graphic = 0
        self.rect = Pygame.rect((pos[0], pos[1], 32, 32))
    def update(self):
        pass
    def draw(self):
        return self.rect, self.graphic

