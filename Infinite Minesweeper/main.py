# Jonas Fairchild, Infinite Minesweeper

# Ensures that pygame exists before trying to use it.
running = True
try:
    import pygame
except:
    print("Failed to import pygame. Type 'pip install pygame' into the terminal.")
    running = False

class Game:
    """Main class"""
    def run(self):
        """Runs the game"""
        from Menus.start import Start
        #from Menus.leaderboard import Leaderboard
        #from Menus.options import Options

        pygame.init()
        screen = pygame.display.set_mode((1200, 1200))
        start = Start(screen, 0.15)
        mouse = pygame.mouse.get_pos()

        running = True
        while running:
            # Events
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    running = False
                    
                start.handleEvent(event)

            new_mouse = pygame.mouse.get_pos()

            start.draw(mouse, new_mouse)
            pygame.display.flip()

            mouse = pygame.mouse.get_pos()

if __name__ == "__main__" and running:
    game = Game()
    game.run()