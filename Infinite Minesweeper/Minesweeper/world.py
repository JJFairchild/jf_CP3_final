import math

from Minesweeper.board_manager import BoardManager
from Minesweeper.camera import Camera
from Miscellaneous.helpers import area

import pygame

class World:
    """Handles Infinite Minesweeper logic"""
    def __init__(self, seed, mine_prob):
        """Initializes necessary components for use in World methods."""
        self.seed = seed
        self.mine_prob = mine_prob
        self.tiles = {}
        self.game_over = False
        self.scrolling = True
        self.dragging = False
        self.manager = BoardManager(self.tiles, seed, mine_prob)
        self.camera = Camera()

    def directRev(self, x, y):
        """Directly reveals a single tile. Also capable of calling floodRev()."""
        if self.game_over:
            return

        tile = self.manager.getTile(x,y)
        mines = self.manager.parseNeighbors(x,y)["mines"]

        if not tile.revealed:
            tile.revealed = True
            if tile.mine:
                self.game_over = True
            elif mines == 0:
                self.floodRev(x,y)

    def floodRev(self, x, y):
        """If a tile has 0 surrounding mines, reveals surrounding tiles in a recursive flood effect."""
        if self.game_over:
            return

        stack = [(x, y)]
        while stack: # Uses a stack rather than a for loop for efficiency
            cx, cy = stack.pop()
            tile = self.manager.getTile(cx, cy)
            if tile.revealed or tile.flagged: # Skip flags already revealed or flagged for efficiency
                continue

            tile.revealed = True
            if tile.mine:
                self.game_over = True
                return

            mines = self.manager.parseNeighbors(cx, cy)["mines"]
            if mines == 0:
                for i, j in area(cx, cy):
                    stack.append((i, j))

    def chordRev(self, x, y):
        """Reveals surrounding tiles of an already revealed tile whose flag quota has been met."""
        tile = self.manager.getTile(x,y)
        flags = self.manager.parseNeighbors(x,y)["flags"]
        mines = self.manager.parseNeighbors(x,y)["mines"]

        if tile.revealed and flags == mines:
            for i, j in area(x, y):
                neighbor = self.manager.getTile(i, j)
                if not neighbor.flagged and not neighbor.revealed:
                    self.directRev(i, j)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print(self.camera.stow(pos[0],pos[1]))
            if event.button == 3:
                self.dragging = True

        if event.type == pygame.MOUSEWHEEL:
            self.scrolling = True
            pos = pygame.mouse.get_pos()
            self.camera.scroll(event.y, pos[0],pos[1])

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            self.dragging = False

    def draw(self, screen, mouse, new_mouse):
        """Draws the viewable world on the screen"""
        if (self.dragging and mouse != new_mouse) or self.scrolling:
            # Drag movement
            self.camera.x += (mouse[0] - new_mouse[0])
            self.camera.y += (mouse[1] - new_mouse[1])

            self.scrolling = False
            screen.fill((50,50,50))
            for x in range(math.floor(1200/(self.camera.spacing))+2):
                for y in range(math.floor(1200/(self.camera.spacing))+2):
                    pygame.draw.rect(screen, (200,200,200), (x*self.camera.spacing - self.camera.x%self.camera.spacing, y*self.camera.spacing - self.camera.y%self.camera.spacing, self.camera.tile_size, self.camera.tile_size))
