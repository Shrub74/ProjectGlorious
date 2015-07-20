#-------------------------------------------------------------------------------
# Project Glorious
#
#
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
from player import *
from skills import *
from environment import *
from Map import *

RESOLUTION = (1024, 768)
FPS = 30
SPLASH_SCREEN = 0
MAIN_MENU = 1
GAME_SCREEN = 2
PAUSE_SCREEN = 3

class MainGame(object):
    def __init__(self):
        # Initialise pygame
        pygame.init()
        # Create FPS clock
        self.clock = pygame.time.Clock()

        # Create screen
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Project Glorious")

        # Create surfaces
        self.tileLayer = pygame.Surface(RESOLUTION)
        #self.objectLayer = pygame.Surface(RESOLUTION)
        self.spriteLayer = pygame.Surface(RESOLUTION)
        #self.hudLayer = pygame.Surface(RESOLUTION)
        #self.textLayer = pygame.Surface(RESOLUTION)

        self.tileLayer.set_colorkey((1, 1, 1))
        self.spriteLayer.set_colorkey((1, 1, 1))

        # Create Map with size 16
        self.map = Map(16)
        self.map.generateTest()
        self.origin = ((RESOLUTION[0]/2) - (self.map.size*32 / 2),
                       (RESOLUTION[1]/2) - (self.map.size*32 / 2))
        self.scrollspeed = 5
        self.screenlock = False

        # Initialise object lists
        self.TileArray = []
        self.ObjectList = []
        self.SpriteList = []

        self.WallGraphic = pygame.image.load('wall.png')
        self.WallGraphic.convert_alpha(self.tileLayer)
        self.FloorGraphic = pygame.image.load('floor.png')
        self.FloorGraphic.convert_alpha(self.tileLayer)
        self.PlayerGraphic = pygame.image.load('warrior.png')
        self.PlayerGraphic.convert_alpha(self.spriteLayer)

        # Create player sprite
        self.player = Player(1, (self.map.size/2, self.map.size/2))
        self.SpriteList.append(self.player)

        # Set MainLoop switch
        self.running = True

        # Set current screen to intro menu
        self.currentScreen = SPLASH_SCREEN
        
    def MainLoop(self):
        # Loop while the game is meant to be looping
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.quitGame()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass

            if event.type == KEYDOWN:
                # Movement Keys
                if event.key == K_UP:
                    if (self.player.pos[0], self.player.pos[1] - 1) not in self.map.WallList:
                        self.player.moveUp()
                if event.key == K_DOWN:
                    if (self.player.pos[0], self.player.pos[1] + 1) not in self.map.WallList:
                        self.player.moveDown()
                if event.key == K_LEFT:
                    if (self.player.pos[0] - 1, self.player.pos[1]) not in self.map.WallList:
                        self.player.moveLeft()
                if event.key == K_RIGHT:
                    if (self.player.pos[0] + 1, self.player.pos[1]) not in self.map.WallList:
                        self.player.moveRight()

                # Weapon
                if event.key == K_SPACE:
                    pass
                
                # Skill Keys
                if event.key == K_a:
                    print('a')
                if event.key == K_s:
                    pass
                if event.key == K_d:
                    pass
                if event.key == K_f:
                    pass
                
    def update(self):
        if self.currentScreen == 0:
            pass
        if self.currentScreen == 1:
            pass
        if self.currentScreen == 2:
            pass
        if self.currentScreen == 3:
            pass

        if not self.screenlock:
            self.mousepos = pygame.mouse.get_pos()
            if self.mousepos[0] > (RESOLUTION[0] - (RESOLUTION[0] * 0.05)):
                self.origin = (self.origin[0] - self.scrollspeed, self.origin[1])
            if self.mousepos[1] > (RESOLUTION[1] - (RESOLUTION[1] * 0.05)):
                self.origin = (self.origin[0], self.origin[1] - self.scrollspeed)
            if self.mousepos[0] < (RESOLUTION[0] * 0.05):
                self.origin = (self.origin[0] + self.scrollspeed, self.origin[1])
            if self.mousepos[1] < (RESOLUTION[1] * 0.05):
                self.origin = (self.origin[0], self.origin[1] + self.scrollspeed)
    
    def draw(self):
        # Refresh screen into black
        self.screen.fill([0, 0, 0])
        self.tileLayer.fill([1, 1, 1])
        self.spriteLayer.fill([1, 1, 1])

        for this in self.SpriteList:
            this.draw()
        for this in self.ObjectList:
            this.draw()

        # Draw map
        for tile in self.map.WallList:
            # Screen position is the Map Origin, plus the Map Co-ordinate
            pos = ((self.origin[0] + (tile[0] - 1) * 32),
                   (self.origin[1] + (tile[1] - 1) * 32))
            self.tileLayer.blit(self.WallGraphic, pos)

        for tile in self.map.FloorList:
            pos = ((self.origin[0] + (tile[0] - 1) * 32),
                   (self.origin[1] + (tile[1] - 1) * 32))
            self.tileLayer.blit(self.FloorGraphic, pos)

        pos = ((self.origin[0] + (self.player.pos[0] - 1) * 32),
               (self.origin[1] + (self.player.pos[1] - 1) * 32))
        self.spriteLayer.blit(self.PlayerGraphic, pos)

        self.screen.blit(self.tileLayer, (0,0))
        self.screen.blit(self.spriteLayer, (0,0))
        
        pygame.display.update()
        
    def quitGame(self):
        pygame.quit()
        sys.exit()


class Connection(object):
    def __init__(self, cid):
        pass
        

game = MainGame()
game.MainLoop()
