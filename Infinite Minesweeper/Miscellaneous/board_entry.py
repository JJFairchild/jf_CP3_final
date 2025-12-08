import math

class Entry:
    """Represents an individual entry on the leaderboard."""
    def __init__(self, user, start_time, tiles, time, mines):
        """Initializes values and calculates overall score."""
        self.user = user
        self.start_time = start_time
        self.tiles = tiles
        self.time = time
        self.mines = mines
        self.score = math.sqrt(tiles * mines) / time