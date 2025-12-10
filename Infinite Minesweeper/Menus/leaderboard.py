from Menus.menu import Menu
from Miscellaneous.file_handling import *

class Leaderboard(Menu):
    """Class for the leaderboard menu"""
    def __init__(self):
        """Initializes necessary values."""
        self.leaderboard = readLeaderboard()
    
    def draw(self, screen):
        """Draws the leaderboard on the screen"""
        pass