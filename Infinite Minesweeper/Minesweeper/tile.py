class Tile:
    """Creates a base tile class for use in World methods."""
    def __init__(self, x, y, mine):
        """Initializes default tile variables."""
        self.x = x
        self.y = y
        self.mine = mine
        self.revealed = False
        self.flagged = False