# Jonas Fairchild, Infinite Minesweeper

# Ensures that pygame exists before trying to use it.
running = True
try:
    import pygame
except:
    print("Failed to import pygame. Type 'pip install pygame' into the terminal.")
    running = False

from Menus.start import Start
#from Menus.leaderboard import Leaderboard
#from Menus.options import Options

class Game:
    def run(self):
        while running:
            # Events
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

if __name__ == "main":
    Game.run()