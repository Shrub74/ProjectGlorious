#-------------------------------------------------------------------------------
# Environment Objects
# 11/7/15
#-------------------------------------------------------------------------------

import pygame

class EnvironmentObject(object):
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class Wall(object):
    def __init__(self, pos):
        self.graphic = 0
        self.rect = pygame.rect((pos, (32, 32)))

class Key(object):
    def __init__(self, pos):
        self.rect = pygame.Rect((pos[0], pos[1]), (24, 24))
        self.tile = 7
    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.inventory.append(1)
            return 'del'
    def draw(self):
        pass
    
class Door(object):
    def __init__(self, pos, locked):
        self.rect = pygame.Rect((pos, (32, 32)))
        self.locked = locked
        self.tile = 4
    def openDoor(self, player):
        # Method for dealing with the opening of the door
        if 'lockpick' in player.skills:
            player.picklock()
        if 1 in player.inventory:
            return True
    def update(self, player):
        if self.rect.colliderect(player.rect):
            if self.openDoor(player):
                return 'del'
    def draw(self):
        pass

class Container(object):
    def __init__(self, pos, contents=[0]):
        # Pos is the container's position on the Map object
        self.rect = pygame.Rect(pos, (32, 32))
        # Contents is a list of Item objects
        self.contents = contents
        if self.contents:
            self.tile = 6
        else:
            self.content = 5
            
    def update(self):
        pass
    def draw(self):
        pass

class Stairs(object):
    def __init__(self, pos, up):
        self.rect = pygame.Rect(pos, (32, 32))
        self.up = up
        if up:
            self.tile = 3
        else:
            self.tile = 2
    def update(self, player):
        pass
