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
    def run(self, running):
        if running:
            pygame.init()
            screen = pygame.display.set_mode((1200, 1200))
            mouse = pygame.mouse.get_pos()
            start = Start(screen, 0.15)

        while running:
            new_mouse = pygame.mouse.get_pos()
            # Events
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    running = False
                    
                start.handleEvent(event)

            start.draw(mouse, new_mouse)
            pygame.display.flip()
            mouse = pygame.mouse.get_pos()

if __name__ == "__main__":
    game = Game()
    game.run(running)