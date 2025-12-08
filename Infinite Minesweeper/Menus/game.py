import random
import time

from Menus.menu import Menu
from Minesweeper.world import World
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox
from Miscellaneous.file_handling import *

class Game(Menu):
    """Handles switching between the start game screen and the world"""
    def __init__(self, screen, mine_prob, tiles={}, start_time=time.time(), seed="", tilecount=0, timer=0, mines=0, origin=False):
        """Initializes necessary values and objects"""
        self.screen = screen
        self.started = False
        self.world = World(seed, mine_prob, tiles, start_time, tilecount, timer, mines, origin)
        self.seedbox = TextBox(300, 450, 600, 60, mutable=True, limit=25)
        self.button = Button(350, 570, 500, 80, text="Generate seed for me", size=50)
        self.quit = Button(900, 1105, 280, 75, (75,75,75), "Save and exit", (200,200,200), 50)
        self.back = Button(50, 50, 100, 50, text="Back", size=50)

    def handleEvent(self, event, mouse):
        """Handles incoming events and forks them to either the world or menu depending on which is being used"""
        if self.started:
            if not self.quit.collidepoint(mouse):
                self.world.handleEvent(event)

            if self.world.game_over:
                pass # handle events for game over ui here
            else:
                if self.quit.handleEvent(event):
                    writeGame(self.world.tiles, self.start_time, self.world.seed, self.world.tilecount, self.world.timer, self.world.flagcount, self.world.manager.origin)
                    return "refresh"

        else:
            self.seedbox.handleEvent(event)

            if self.button.handleEvent(event):
                if self.button.text == "Generate seed for me":
                    seed = str(random.randint(-1000000, 1000000))
                else:
                    seed = self.seedbox.text
                self.world.seed = seed
                self.started = True
                self.start_time = time.time()
                print(self.world.seed)
            
            if self.back.handleEvent(event):
                return "start"

        return "game"

    def draw(self, mouse, new_mouse):
        """Draws either the world or the start menu on the screen depending on which is being used."""
        if self.started:
            self.world.draw(self.screen, mouse, new_mouse)

            if self.world.game_over:
                pass # draw game over ui here
            else:
                self.quit.draw(self.screen)
        else:
            if self.seedbox.text == "" and self.button.text != "Generate seed for me":
                self.button = Button(350, 570, 500, 80, text="Generate seed for me", size=50)

            elif self.seedbox.text != "" and self.button.text != "Start":
                self.button = Button(350, 570, 500, 80, text="Start", size=50)

            self.screen.fill((60,60,60))
            self.button.draw(self.screen)
            self.back.draw(self.screen)
            self.seedbox.draw(self.screen)