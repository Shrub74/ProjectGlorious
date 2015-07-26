import pygame

class Player(object):
    def __init__(self, ident, pos):
        # Player's ID ingame, between 1 to 4
        self.id = ident
        self.rect = pygame.Rect(pos, (28, 28))
        self.skills = [0, 0, 0, 0]
        self.attacking = False
        self.speed = 3
        self.inventory = []
    def update(self):
        pass
    def draw(self):
        pass

    def moveUp(self):
        #self.pos = (self.pos[0], self.pos[1] - self.speed)
        self.rect.move_ip(0, -self.speed)
    def moveDown(self):
        #self.pos = (self.pos[0], self.pos[1] + self.speed)
        self.rect.move_ip(0, self.speed)
    def moveLeft(self):
        #self.pos = (self.pos[0] - self.speed, self.pos[1])
        self.rect.move_ip(-self.speed, 0)
    def moveRight(self):
        #self.pos = (self.pos[0] + self.speed, self.pos[1])
        self.rect.move_ip(self.speed, 0)

    def canMove(self):
        pass

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
