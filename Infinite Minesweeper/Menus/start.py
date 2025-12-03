from Menus.menu import Menu
from Miscellaneous.button import Button
from Miscellaneous.file_handling import *

import pygame

class Start(Menu):
    def __init__(self, screen):
        self.screen = screen
        self.savedgame = False
        self.newgame = Button(350, 570, 500, 80, text="New Game", size=50)

    def handleEvent(self, event):
        pass

    def draw(self):
        self.screen.fill((60,60,60))