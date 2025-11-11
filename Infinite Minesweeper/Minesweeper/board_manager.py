import random

from tile import Tile
from main import area

class BoardManager:
    def __init__(self, tiles, seed, mine_prob):
        self.tiles = tiles
        self.seed = seed
        self.mine_prob = mine_prob

    def isMine(self, x, y):
        r = random.Random(f"{self.seed}:{x}:{y}") # Deterministic randomness based on seed, x, and y.
        return r.random() < self.mine_prob

    def getTile(self, x, y):
        tile = self.tiles.get((x, y))
        if tile:
            return self.tiles[(x,y)]
        else:
            tile = Tile(x, y, self.isMine(x, y))
            self.tiles[(x, y)] = tile
            return tile
        
    def parseNeighbors(self,x,y):
        mines = 0
        flags = 0
        
        for index in area(x,y):
            tile = self.getTile(index)
            if tile.mine:
                mines += 1
            if tile.flagged:
                flags += 1

        return {"mines":mines, "flags":flags}