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
        self.objectLayer = pygame.Surface(RESOLUTION)
        self.spriteLayer = pygame.Surface(RESOLUTION)
        self.hudLayer = pygame.Surface(RESOLUTION)
        self.textLayer = pygame.Surface(RESOLUTION)

        # Initialise object lists
        self.TileArray = []
        self.ObjectList = []
        self.SpriteList = []

        # Create player sprite
        player = Player(0, (500, 300))
        self.SpriteList.append(player)

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
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_LEFT:
                    pass
                if event.key == K_RIGHT:
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
    
    def draw(self):
        # Refresh screen into black
        self.screen.fill([0, 0, 0])

        for this in self.SpriteList:
            this.draw()
        for this in self.ObjectList:
            this.draw()

        
        pygame.display.update()
        
    def quitGame(self):
        pygame.quit()
        sys.exit()


class Connection(object):
    def __init__(self, cid):
        pass
        

game = MainGame()
game.MainLoop()
