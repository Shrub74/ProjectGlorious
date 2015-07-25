#-------------------------------------------------------------------------------
# Map module for ProjectGlorious
# 15/7/15
#
#-------------------------------------------------------------------------------

from random import randint

class Map(object):
    """
    This is the map object that gets written to the game layers
    It is made up of a matrix of a defined size (usually 128x128) of
    tiles and objects
    """
    def __init__(self, size):
        self.size = size

        # Wall and Floor Lists are just co-ordinate lists for the draw function
        self.WallList = []
        self.FloorList = []

        # Object and Sprite lists are lists of objects
        self.ObjectList = []
        self.SpriteList = []
        
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
        asciimap = ['XXXXXXXX',
                    'XX.....X',
                    'X.XXXX.X',
                    'X......X',
                    'X......X',
                    'X......X',
                    'X....X.X',
                    'XXXXXXXX']
        
        for line in asciimap:
            for x in range(0, len(line)):
                if line[x] == 'X':
                    self.WallList.append((x,y))
                if line[x] == '.':
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
