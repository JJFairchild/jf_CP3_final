from board_manager import BoardManager
from tile import Tile
from main import area

class World:
    def __init__(self, seed, mine_prob):
        self.seed = seed
        self.mine_prob = mine_prob
        self.tiles = []
        self.game_over = False
        self.manager = BoardManager(self.tiles, seed, mine_prob)

    def directRev(self, x, y):
        tile = self.manager.getTile(x,y)
        flags = self.manager.parseNeighbors(x,y)["flags"]
        mines = self.manager.parseNeighbors(x,y)["mines"]
        neighbors = []
        for i in area(x,y):
            neighbors.append(self.manager.getTile(i))

        if mines == 0:
            self.floodRev(x,y)

    def floodRev(self, x, y):
        pass

    def chordRev(self, x, y):
        tile = self.manager.getTile(x,y)
        flags = self.manager.parseNeighbors(x,y)["flags"]
        mines = self.manager.parseNeighbors(x,y)["mines"]
        neighbors = []
        for i in area(x,y):
            neighbors.append(self.manager.getTile(i))

        if tile.revealed and flags == mines:
            for neighbor in neighbors:
                if not neighbor.flagged and not neighbor.revealed:
                    neighbor.directRev(x,y)
