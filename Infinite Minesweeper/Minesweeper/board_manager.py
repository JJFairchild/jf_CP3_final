import random

from tile import Tile

class BoardManager:
    def __init__(self, tiles, seed, mine_prob):
        self.tiles = tiles
        self.seed = seed
        self.mine_prob = mine_prob

    def isMine(self, x, y):
        r = random.Random(f"{self.seed}:{x}:{y}")
        return r.random() < self.mine_prob

    def getTile(self, x, y):
        if self.tiles[(x,y)]:
            return self.tiles[(x,y)]
        else:
            return Tile(x, y, self.isMine(x, y))