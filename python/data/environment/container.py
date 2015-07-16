class Container(EnvironmentObject):
    def __init__(self, pos, contents=[0]):
        # Pos is the container's position on the Map object
        self.pos = pos
        # Contents is a list of Item objects
        self.contents = contents
    def update(self):
        pass
    def draw(self):
        pass
