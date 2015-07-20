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
