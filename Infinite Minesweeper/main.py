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

if running:
    screen = pygame.display.set_mode((1200, 1200))
    start = Start(screen, 0.15)

class Game:
    def run(self, running):
        while running:
            # Events
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    running = False

            start.draw()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run(running)