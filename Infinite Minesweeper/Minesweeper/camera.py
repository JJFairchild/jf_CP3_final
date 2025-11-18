import math

class Camera:
    """Calculates where the screen should be displayed from coordinates in the minesweeper game"""
    def __init__(self):
        """Initializes values that the camera uses for coordinate calculation"""
        self.x = -600
        self.y = -600
        self.tile_size = 100
        self.spacing = self.tile_size*9/8

    def wtos(self, x,y):
        pass

    def stow(self, x,y):
        pos = ((x+self.x)/self.spacing, (y+self.y)/self.spacing)
        return (math.floor(pos[0]), math.floor(pos[1]))

    def pan(self, mouse, new_mouse):
        self.x += (mouse[0] - new_mouse[0])
        self.y += (mouse[1] - new_mouse[1])

    def zoom(self):
        pass