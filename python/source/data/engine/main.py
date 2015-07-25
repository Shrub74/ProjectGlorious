#-------------------------------------------------------------------------------
# Project Glorious
#
#
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
from player import *
from skills import *
from Map import *
from environment import *
from wall import *

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
        self.showFPS = False

        # Create screen
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Project Glorious")

        # Create surfaces
        self.tileLayer = pygame.Surface(RESOLUTION)
        #self.objectLayer = pygame.Surface(RESOLUTION)
        self.spriteLayer = pygame.Surface(RESOLUTION)
        self.hudLayer = pygame.Surface(RESOLUTION)
        #self.textLayer = pygame.Surface(RESOLUTION)

        self.tileLayer.set_colorkey((1, 1, 1))
        self.spriteLayer.set_colorkey((1, 1, 1))
        self.hudLayer.set_colorkey((1, 1, 1))

        # Create Map with size 16
        self.map = Map(8)
        #self.map.generateTest()
        self.map.loadTest()

        self.font = pygame.font.Font(None, 32)

        # Create Wall objects from map walllist
        self.WallList = []
        for pos in self.map.WallList:
            wall = pygame.Rect(((pos[0]-1)*32, (pos[1]-1)*32), (32, 32))
            self.WallList.append(wall)

        self.origin = ((RESOLUTION[0]/2) - (self.map.size*32 / 2),
                       (RESOLUTION[1]/2) - (self.map.size*32 / 2))
        

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

        pygame.key.set_repeat(1, 20)

        # Create player sprite
        self.player = Player(1, ((self.map.size/2) * 32, (self.map.size/2)*32))
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
                    ghostRect = self.player.rect.move(0, -self.player.speed)
                    canMove = True
                    for wall in self.WallList:
                        if ghostRect.colliderect(wall):
                            canMove = False
                            pos = wall.y + 32
                    if canMove:
                        self.player.moveUp()
                    else:
                        self.player.rect.y = pos
                if event.key == K_DOWN:
                    ghostRect = self.player.rect.move(0, self.player.speed)
                    canMove = True
                    for wall in self.WallList:
                        if ghostRect.colliderect(wall):
                            canMove = False
                            pos = wall.y - 30
                    if canMove:
                        self.player.moveDown()
                    else:
                        self.player.rect.y = pos
                if event.key == K_LEFT:
                    ghostRect = self.player.rect.move(-self.player.speed, 0)
                    canMove = True
                    for wall in self.WallList:
                        if ghostRect.colliderect(wall):
                            canMove = False
                            pos = wall.x + 34
                    if canMove:
                        self.player.moveLeft()
                    else:
                        self.player.rect.x = pos
                if event.key == K_RIGHT:
                    ghostRect = self.player.rect.move(self.player.speed, 0)
                    canMove = True
                    for wall in self.WallList:
                        if ghostRect.colliderect(wall):
                            canMove = False
                            pos = wall.x - 28
                    if canMove:
                        self.player.moveRight()
                    else:
                        self.player.rect.x = pos

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

                if event.key == K_F9:
                    self.showFPS = not self.showFPS
                
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
        self.tileLayer.fill([1, 1, 1])
        self.spriteLayer.fill([1, 1, 1])
        self.hudLayer.fill([1, 1, 1])

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

        # Draw player
        pos = ((self.origin[0] + (self.player.rect[0] - 4)),
               (self.origin[1] + (self.player.rect[1] - 4)))
        self.spriteLayer.blit(self.PlayerGraphic, pos)

        if self.showFPS:
            fps = str(int(self.clock.get_fps()))
            self.hudLayer.blit(self.font.render(fps, True, [255, 255, 255]),
                               (8, 8))
        
        self.screen.blit(self.tileLayer, (0,0))
        self.screen.blit(self.spriteLayer, (0,0))
        self.screen.blit(self.hudLayer, (0, 0))
        
        pygame.display.update()
        
    def quitGame(self):
        pygame.quit()
        sys.exit()


class Connection(object):
    def __init__(self, cid):
        pass
        
game = MainGame()
game.MainLoop()
