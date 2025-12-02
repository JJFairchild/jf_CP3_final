import random
import time

from Menus.menu import Menu
from Minesweeper.world import World
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox

class Game(Menu):
    """Handles switching between the start game screen and the world"""
    def __init__(self, screen, mine_prob):
        """Initializes necessary values and objects"""
        self.screen = screen
        self.mine_prob = mine_prob
        self.started = False
        self.seed = ""
        self.seedbox = TextBox(300, 450, 600, 60, mutable=True, limit=25)
        self.button = Button(350, 570, 500, 80, text="Generate seed for me", size=50)
        self.back = Button(20,20, 100, 50, text="Back", size=50)

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
                self.start_time = time.time()
            
            if self.back.handleEvent(event):
                pass

    def draw(self, mouse, new_mouse):
        """Draws either the world or the start menu on the screen depending on which is being used."""
        if self.started:
            self.world.draw(self.screen, mouse, new_mouse, self.start_time)
        else:
            if self.seedbox.text == "" and self.button.text != "Generate seed for me":
                self.button  = Button(350, 570, 500, 80, text="Generate seed for me", size=50)

            elif self.seedbox.text != "" and self.button.text != "Start":
                self.button  = Button(350, 570, 500, 80, text="Start", size=50)

            self.screen.fill((60,60,60))
            self.button.draw(self.screen)
            self.back.draw(self.screen)
            self.seedbox.draw(self.screen)