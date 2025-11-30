import random

from Menus.menu import Menu
from Minesweeper.world import World
from Minesweeper.camera import Camera
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox

class Start(Menu):
    """Handles switching between the start game screen and the world"""
    def __init__(self, screen, mine_prob):
        """Initializes necessary values and objects"""
        self.screen = screen
        self.mine_prob = mine_prob
        self.started = False
        self.seed = ""
        self.seedbox = TextBox(100, 300, 300, 50, mutable=True, color=(255,255,255), text_color=(0,0,0), limit=20)
        self.button = Button(400, 560, 400, 80, text="Generate seed for me")

    def handleEvent(self, event):
        """Handles incoming events and forks them to either the world or menu depending on which is being used"""
        if self.started:
            self.world.handleEvent(event)
        else:
            self.seedbox.handleEvent(event)
            if self.button.handleEvent(event):
                if self.button.text == "Generate seed for me":
                    self.seed = str(random.randint(-1000000, 1000000))
                else:
                    self.seed = self.seedbox.text
                self.world = World(self.seed, self.mine_prob)
                self.started = True

    def draw(self, mouse, new_mouse):
        """Draws either the world or the start menu on the screen depending on which is being used."""
        if self.started:
            self.world.draw(self.screen, mouse, new_mouse)
        else:
            if self.seedbox.text == "" and self.button.text != "Generate seed for me":
                self.button = Button(400, 560, 400, 80, text="Generate seed for me")

            elif self.seedbox.text != "" and self.button.text != "Start":
                self.button = Button(475, 560, 250, 80, text="Start")

            self.button.draw(self.screen)
            self.seedbox.draw(self.screen)

