# Might null the Wall object and just make a list of walls
import pygame

class Wall(object):
    def __init__(self, pos):
        self.graphic = 0
        self.rect = pygame.rect((pos, (32, 32)))

