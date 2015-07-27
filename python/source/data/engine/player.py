import pygame

class Player(object):
    def __init__(self, ident, pos, sprite_image):
        # Player's ID ingame, between 1 to 4
        self.id = ident
        self.rect = pygame.Rect(pos, (28, 28))
        self.skills = [0, 0, 0, 0]
        self.attacking = False
        self.speed = 3
        self.direction = True
        self.animation = 0
        self.inventory = []
        self.spriteset = []
        self.footstep = pygame.mixer.Sound('step.wav')
        self.getSprite(sprite_image)
    def update(self):
        if self.animation > 40:
            self.animation = 0
#        if self.animation % 5 == 0:
#            self.footstep.play()
    def draw(self):
        pass

    def moveUp(self):
        self.rect.move_ip(0, -self.speed)
        self.animation += 1
    def moveDown(self):
        self.rect.move_ip(0, self.speed)
        self.animation += 1
    def moveLeft(self):
        # If facing right, turn left
        if self.direction:
            self.direction = not self.direction
        self.rect.move_ip(-self.speed, 0)
        self.animation += 1
    def moveRight(self):
        if not self.direction:
            self.direction = not self.direction
        self.rect.move_ip(self.speed, 0)
        self.animation += 1

    def canMove(self):
        pass

    def getSprite(self, sprite_image):
        spriteset = pygame.image.load(sprite_image).convert()
        width, height = spriteset.get_size()
        rows = int(height/32)
        cols = int(width/32)
        for sprite_y in range(0, rows):
            for sprite_x in range(0, cols):
                rect = (sprite_x*32, sprite_y*32, 32, 32)
                self.spriteset.append(spriteset.subsurface(rect))

    def getFrame(self, ticker):
        if self.direction:
            if self.animation < 20:
                return self.spriteset[0]
            else:
                return self.spriteset[1]
        else:
            if self.animation < 20:
                return self.spriteset[2]
            else:
                return self.spriteset[3]

    def swing(self):
        """
        Causes the player to attack with
        their weapon
        """
        # Begin the attacking procedure
        # Determine attacking animation frame range based on speed
        # Allow checking for rect collisions with attacking flag
        # End attacking flag after animation frame range reached.
        
        #self.attacking = True
        #self.attacking = False
