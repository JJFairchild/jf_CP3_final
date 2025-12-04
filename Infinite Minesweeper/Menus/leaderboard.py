from Menus.menu import Menu
from Miscellaneous.file_handling import *

class Leaderboard(Menu):
    """Class for the leaderboard menu"""
    def __init__(self, screen):
        """Initializes necessary values."""
        self.screen = screen
        self.leaderboard = readLeaderboard()
    
    def draw(self):
        """Draws the leaderboard on the screen"""
        pass