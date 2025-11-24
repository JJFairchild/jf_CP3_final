import random

from Menus.menu import Menu
from Minesweeper.world import World
from Minesweeper.camera import Camera
from Miscellaneous.button import Button
from Miscellaneous.textbox import TextBox

class Start(Menu):
    def __init__(self, screen, mine_prob):
        self.screen = screen
        self.mine_prob = mine_prob
        self.started = False
        self.seed = ""
        self.seedbox = TextBox(100, 300, 300, 50, mutable=True, color=(255,255,255), text_color=(0,0,0), limit=20)
        self.button = Button(150, 200, 150, 60, color=(255,255,255), text_color=(0,0,0), text="Generate seed\nfor me")
        self.world = World(self.seed, self.mine_prob)

    def handleEvent(self, event):
        self.seedbox.handleEvent(event)
        if self.button.handleEvent(event):
            if self.button.text == "Generate seed\nfor me":
                self.seed = str(random.randint(0, 10000000))
            else:
                self.seed = self.seedbox.text
            self.started = True
            self.start()
        if self.started:
            self.world.handleEvent(event)

    def start(self):
        if self.seed != "":
            pass

    def draw(self, mouse, new_mouse):
        if self.started:
            self.world.draw(self.screen, mouse, new_mouse)
        else:
            if self.seedbox.text == "":
                self.button.text = "Generate seed\nfor me"
            else:
                self.button.text = "Start"

            self.button.draw(self.screen)
            self.seedbox.draw(self.screen)

