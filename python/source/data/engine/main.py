#-------------------------------------------------------------------------------
# Project Glorious
#
#
#-------------------------------------------------------------------------------

import pygame, sys
import random
from pygame.locals import *
from player import *
from skills import *
from Map import *
from environment import *

RESOLUTION = (1024, 768)
FPS = 60
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
        self.ticker = 0

        # Create screen
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Project Glorious")

        # Create surfaces
        self.tileLayer = pygame.Surface(RESOLUTION)
        self.objectLayer = pygame.Surface(RESOLUTION)
        self.spriteLayer = pygame.Surface(RESOLUTION)
        self.hudLayer = pygame.Surface(RESOLUTION)
        #self.textLayer = pygame.Surface(RESOLUTION)

        self.tileLayer.set_colorkey((1, 1, 1))
        self.spriteLayer.set_colorkey((1, 1, 1))
        self.hudLayer.set_colorkey((1, 1, 1))
        self.objectLayer.set_colorkey((1, 1, 1))

        # Create Map with size 16
        self.map = Map(8, 'demotileset.png')
        #self.map.generateTest()
        self.map.loadTest()

        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Create Wall objects from map walllist
        self.WallList = []
        # Initialise object lists
        self.TileArray = []
        self.ObjectList = []
        self.SpriteList = []
        for pos in self.map.WallList:
            wall = pygame.Rect(((pos[0]-1)*32, (pos[1]-1)*32), (32, 32))
            self.WallList.append(wall)

        # Objects
        for pos in self.map.KeyList:
            key = Key(((pos[0] - 1) * 32, (pos[1] - 1) * 32))
            self.ObjectList.append(key)
        for pos in self.map.DoorList:
            door = Door(((pos[0] - 1) * 32, (pos[1] - 1) * 32), False)
            self.ObjectList.append(door)
        for pos in self.map.ChestList:
            chest = Container(((pos[0] - 1) * 32, (pos[1] - 1) * 32), 0)
            self.ObjectList.append(chest)
        for pos in self.map.UpstairsList:
            upstairs = Stairs(((pos[0] - 1) * 32, (pos[1] - 1) * 32), True)
            self.ObjectList.append(upstairs)
        for pos in self.map.DownstairsList:
            downstairs = Stairs(((pos[0] - 1) * 32, (pos[1] - 1) * 32), False)
            self.ObjectList.append(downstairs)

        self.origin = ((RESOLUTION[0]/2) - (self.map.size*32 / 2),
                       (RESOLUTION[1]/2) - (self.map.size*32 / 2))

        pygame.key.set_repeat(1, 20)

        # Create player sprite
        print(self.map.UpstairsList)
        pos = ((self.map.UpstairsList[0][0] - 1) * 32,
               (self.map.UpstairsList[0][1] - 1) * 32)
        modifier = random.randint(0,3)
        print(modifier)
        if modifier == 0:
            pos = (pos[0], pos[1] - 32)
        if modifier == 1:
            pos = (pos[0] - 32, pos[1])
        if modifier == 2:
            pos = (pos[0] + 32, pos[1])
        if modifier == 3:
            pos = (pos[0], pos[1] + 32)
        self.player = Player(1, pos, 'player.png')
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
        
        for obj in self.ObjectList:
            if obj.update(self.player) == 'del':
                self.ObjectList.remove(obj)

        self.player.update()

        self.ticker += 1
        if self.ticker == 60:
            self.ticker = 0

        if self.player.rect.x + self.origin[0] > (1024 - 128):
            self.origin = (self.origin[0] - 1, self.origin[1])
        if self.player.rect.x + self.origin[0] < (128):
            self.origin = (self.origin[0] + 1, self.origin[1])
    
    def draw(self):
        # Refresh screen into black
        self.screen.fill([0, 0, 0])
        self.tileLayer.fill([1, 1, 1])
        self.objectLayer.fill([1, 1, 1])
        self.spriteLayer.fill([1, 1, 1])
        self.hudLayer.fill([1, 1, 1])

        #for this in self.SpriteList:
        #    this.draw()
        #for this in self.ObjectList:
        #    this.draw()

        # Draw map
        for tile in self.map.WallList:
            # Screen position is the Map Origin, plus the Map Co-ordinate
            pos = ((self.origin[0] + (tile[0] - 1) * 32),
                   (self.origin[1] + (tile[1] - 1) * 32))
            self.tileLayer.blit(self.map.tiles[1], pos)

        for tile in self.map.FloorList:
            pos = ((self.origin[0] + (tile[0] - 1) * 32),
                   (self.origin[1] + (tile[1] - 1) * 32))
            self.tileLayer.blit(self.map.tiles[0], pos)

        for obj in self.ObjectList:
            pos = ((self.origin[0] + (obj.rect[0] - 1)),
                   (self.origin[1] + (obj.rect[1] - 1)))
            self.objectLayer.blit(self.map.tiles[obj.tile], pos)

        # Draw player
        pos = ((self.origin[0] + (self.player.rect[0] - 4)),
               (self.origin[1] + (self.player.rect[1] - 4)))
        self.spriteLayer.blit(self.player.getFrame(self.ticker), pos)

        if self.showFPS:
            fps = str(int(self.clock.get_fps()))
            self.hudLayer.blit(self.font.render(fps, True, [255, 255, 255]),
                               (8, 8))
        
        self.screen.blit(self.tileLayer, (0,0))
        self.screen.blit(self.objectLayer, (0,0))
        self.screen.blit(self.spriteLayer, (0,0))
        self.screen.blit(self.hudLayer, (0, 0))
        
        pygame.display.update()
        
    def quitGame(self):
        pygame.quit()
        sys.exit()

    def load_map(self):
        pass


class Connection(object):
    def __init__(self, cid):
        pass
        
game = MainGame()
game.MainLoop()
