#-------------------------------------------------------------------------------
# ItemSprite
# 16/7/15
#-------------------------------------------------------------------------------

class Item(object):
    """
    Item is the sprite for the item that floats 
    """
    def __init__(self, pos, visibleTo, itemtype, stats=[0]):
        # The position of the sprite on the map
        self.pos = pos
        # Which players the item is visible to
        # This also affects collisions
        self.visibleTo = visibleTo
        # The type of the item
        # 0 = item, 1 = weapon
        self.type = itemtype
        # The stats, if a weapon. If not, it is an item id
        self.stats = stats
        
    def update(self):
        pass
    
    def draw(self):
        pass
