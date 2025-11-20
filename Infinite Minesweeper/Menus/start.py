from menu import Menu
from Minesweeper.world import World

class Start(Menu):
    def __init__(self, mine_prob):
        self.mine_prob = mine_prob
        self.seed = ""

    def start(self):
        if self.seed != "":
            world = World(self.seed, self.mine_prob)

    def draw(self):
        pass