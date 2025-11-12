import random

from tile import Tile
from main import area

class BoardManager:
    """Handles tiles and gathers data about them"""
    def __init__(self, tiles, seed, mine_prob):
        """Initializes needed variables"""
        self.tiles = tiles
        self.seed = seed
        self.mine_prob = mine_prob

    def isMine(self, x, y):
        """Deterministically decides whether a tile is a mine or not."""
        r = random.Random(f"{self.seed}:{x}:{y}") # Deterministic randomness based on seed, x, and y.
        return r.random() < self.mine_prob

    def getTile(self, x, y):
        """Gets a specific tile and makes sure a tile always exists where it is needed."""
        tile = self.tiles.get((x, y))
        if tile:
            return self.tiles[(x,y)]
        else:
            tile = Tile(x, y, self.isMine(x, y))
            self.tiles[(x, y)] = tile
            return tile
        
    def parseNeighbors(self,x,y):
        """Gathers data (mines and flags) about neighboring tiles."""
        mines = 0
        flags = 0
        
        for i,j in area(x,y):
            tile = self.getTile(i,j)
            if tile.mine:
                mines += 1
            if tile.flagged:
                flags += 1

        return {"mines":mines, "flags":flags} # Dictionary for ease of use