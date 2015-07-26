#-------------------------------------------------------------------------------
# Map module for ProjectGlorious
# 15/7/15
#
#-------------------------------------------------------------------------------

from random import randint
import pygame

class Map(object):
    """
    This is the map object that gets written to the game layers
    It is made up of a matrix of a defined size (usually 128x128) of
    tiles and objects
    """
    def __init__(self, size, tile_image):
        self.size = size

        self.tile_image = tile_image

        # Wall and Floor Lists are just co-ordinate lists for the draw function
        self.WallList = []
        self.FloorList = []
        self.KeyList = []
        self.DoorList = []
        self.ChestList = []
        self.DownstairsList = []
        self.UpstairsList = []

        # Object and Sprite lists are lists of objects
        self.ObjectList = []
        self.SpriteList = []

        self.loadTileset()
        
    def update(self):
        pass
    def draw(self):
        pass

    def writeToMap(self):
        """ 
        Writes the DunGen output to the map instance
        """
        pass

    def loadTest(self):
        y = 1
        asciimap = ['XXXXXXXXXXXXXXXX XXX',
                    'X..............X X.X',
                    'X......XXXXXXX.X XXX',
                    'X......X.....X.X',
                    'X......X.X.K.X.X',
                    'X..<...X.XXXXX.XXXXX',
                    'X......X.......D..>X',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX']
        
        for line in asciimap:
            for x in range(0, len(line)):
                if line[x] == 'X':
                    self.WallList.append((x,y))
                if line[x] == '.':
                    self.FloorList.append((x,y))
                if line[x] == 'K':
                    self.KeyList.append((x,y))
                    self.FloorList.append((x,y))
                if line[x] == 'D':
                    self.DoorList.append((x,y))
                    self.FloorList.append((x,y))
                if line[x] == '<':
                    self.UpstairsList.append((x,y))
                    self.FloorList.append((x,y))
                if line[x] == '>':
                    self.DownstairsList.append((x,y))
                if line[x] == 'C':
                    self.ChestList.append((x,y))
                    self.FloorList.append((x,y))

            y = y + 1

    def generateTest(self):
        print('Generating Test')
        # Create surrounding walls
        for x in range(1, self.size):
            self.WallList.append((x, 1))
            self.WallList.append((x, self.size - 1))
        for y in range(2, (self.size - 1)):
            self.WallList.append((1, y))
            self.WallList.append((self.size - 1, y))
        # Create inner floors
        for x in range(2, (self.size - 1)):
            for y in range(2, (self.size - 1)):
                self.FloorList.append((x, y))
        print('Test Generated')

    def loadTileset(self):
        tileset = pygame.image.load(self.tile_image).convert()
        width, height = tileset.get_size()
        self.tiles = []
        rows = int(height/32)
        for tile_y in range(0, rows):
            for tile_x in range(0, 8):
                rect = (tile_x*32, tile_y*32, 32, 32)
                self.tiles.append(tileset.subsurface(rect))
                
