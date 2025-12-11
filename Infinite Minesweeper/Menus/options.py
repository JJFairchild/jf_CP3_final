from Menus.menu import Menu
from Miscellaneous.file_handling import *
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox

class Options(Menu):
    """Class for the leaderboard menu"""
    def __init__(self):
        """Initializes necessary values."""
        self.mine_prob = readOptions()

        self.back = Button(50, 50, 100, 50, text="Back", size=50)
        self.save = Button(1050, 50, 100, 50, text="Save", size=50)
        self.note = TextBox(50,1050,1100,100, False, "Note: Updating options while a game is saved will delete the saved game.", size=40)
    
    def handleEvent(self, event):
        if self.back.handleEvent(event):
            return "start"
        if self.save.handleEvent(event):
            clearGame()
            # UPDATE OPTIONS HERE
        
        return "options"

    def draw(self, screen):
        """Draws the leaderboard on the screen"""
        screen.fill((60,60,60))
        self.back.draw(screen)
        self.save.draw(screen)
        self.note.draw(screen)