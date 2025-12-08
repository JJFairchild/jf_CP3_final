# Jonas Fairchild, Infinite Minesweeper

# Ensures that pygame exists before trying to use it.
run = True
try:
    import pygame
except:
    print("Failed to import pygame. Type 'pip install pygame' into the terminal.")
    run = False

from Miscellaneous.file_handling import *

import time

class Main:
    """Main class"""
    def run(self):
        """Runs the game"""
        from Menus.game import Game
        from Menus.start import Start
        from Menus.leaderboard import Leaderboard
        #from Menus.options import Options

        pygame.init()
        pygame.display.set_caption("Infinite Minesweeper")
        screen = pygame.display.set_mode((1200, 1200))
        mouse = pygame.mouse.get_pos()

        game = Game(screen, 0.15)
        start = Start(screen)
        leaderboard = Leaderboard(screen)

        menu = "start"

        running = True
        while running:
            # Events
            for event in pygame.event.get():
                # Quit game
                if event.type == pygame.QUIT:
                    running = False
                    
                match menu:
                    case "start":
                        menu = start.handleEvent(event)
                        if menu == "quit":
                            running = False
                        if menu == "cont":
                            tiles, start_time, seed, tilecount, timer, mines, origin = readGame()
                            game = Game(screen, 0.15, tiles, start_time-timer, seed, tilecount, timer-time.time(), mines, origin)
                            game.started = True
                            menu = "game"
                    case "game":
                        menu = game.handleEvent(event, mouse)
                        if menu == "refresh":
                            game = Game(screen, 0.15)
                            start.gamesaved = True
                            menu = "start"

            new_mouse = pygame.mouse.get_pos()

            match menu:
                case "start":
                    start.draw()
                case "game":
                    game.draw(mouse, new_mouse)
            pygame.display.flip()

            mouse = pygame.mouse.get_pos()

if __name__ == "__main__" and run:
    Main().run()