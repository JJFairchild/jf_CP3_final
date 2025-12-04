from Menus.menu import Menu
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox
from Miscellaneous.file_handling import *

import pygame

class Start(Menu):
    def __init__(self, screen):
        self.screen = screen
        self.savedgame = readGame()
        self.gamesaved = bool(self.savedgame)
        self.minesweeper = TextBox(200, 100, 800, 100, False, text="Infinite Minesweeper", size=75)
        self.cont = Button(350, 500, 500, 80, text="Continue", size=50)
        self.newgame = Button(350, 600, 500, 80, text="New Game", size=50)
        self.leaderboard = Button(350, 700, 500, 80, text="Leaderboard", size=50)
        self.options = Button(350, 800, 500, 80, text="Options", size=50)
        self.quit = Button(350, 900, 500, 80, text="Quit", size=50)

    def handleEvent(self, event):
        if self.newgame.handleEvent(event):
            return "game"
        if self.quit.handleEvent(event):
            return "quit"
    
        return "start"

    def draw(self):
        self.screen.fill((60,60,60))

        if self.gamesaved:
            self.cont.draw(self.screen)
        self.minesweeper.draw(self.screen)
        self.newgame.draw(self.screen)
        self.leaderboard.draw(self.screen)
        self.options.draw(self.screen)
        self.quit.draw(self.screen)