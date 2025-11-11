# Jonas Fairchild, Infinite Minesweeper

running = True
try:
    import pygame
    import random
except:
    print("Failed to import pygame. Type 'pip install pygame' into the terminal.")
    running = False

def area(x,y):
    area = []
    for x_off in range(-1, 2):
            for y_off in range(-1, 2):
                if (x_off,y_off) != (0,0):
                    area.append((x+x_off,y+y_off))
    return area
                    

while running:
    pass