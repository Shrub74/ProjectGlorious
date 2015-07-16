#-------------------------------------------------------------------------------
# Environment Objects
# 11/7/15
#-------------------------------------------------------------------------------


class EnvironmentObject(object):
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

# Might null the Wall object and just make a list of walls
class Wall(EnvironmentObject):
    def __init__(self, pos):
        self.graphic = 0
        self.rect = Pygame.rect((pos[0], pos[1], 32, 32))
    def update(self):
        pass
    def draw(self):
        return self.rect, self.graphic

class Door(EnvironmentObject):
    def __init__(self, pos, locked):
        self.pos = pos
        self.locked = locked
    def openDoor(self, player):
        # Method for dealing with the opening of the door
        if 'lockpick' in player.skill:
            player.picklock()
    def update(self):
        pass
    def draw(self):
        pass

class Container(EnvironmentObject):
    def __init__(self, pos, contents=[0]):
        # Pos is the container's position on the Map object
        self.pos = pos
        # Contents is a list of Item objects
        self.contents = contents
    def update(self):
        pass
    def draw(self):
        pass
