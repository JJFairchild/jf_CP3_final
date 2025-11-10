class Tile:
    def __init__(self, x, y, mine):
        self.x = x
        self.y = y
        self.mine = mine
        self.revealed = False
        self.flagged = False