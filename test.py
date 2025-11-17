import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1200, 1200))

tile_size = 100
spacing = tile_size*9/8
offset = [0,0]
drag = False
mouse = pygame.mouse.get_pos()

def stow(pos):
    pos = (pos[0]/(spacing), pos[1]/(spacing))
    return (math.floor(pos[0]), math.floor(pos[1]))

running = True
while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(stow(mouse))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            drag = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            drag = False

    new_mouse = pygame.mouse.get_pos()
    if drag and mouse != new_mouse:
        # Drag movement
        offset[0] += (new_mouse[0] - mouse[0])
        offset[1] += (new_mouse[1] - mouse[1])
        mouse = new_mouse

        # Draw screen
        offset[0] += (pygame.mouse.get_pos()[0]-mouse[0])
        offset[1] += (pygame.mouse.get_pos()[1]-mouse[1])
        screen.fill((50,50,50))
        for x in range(math.floor(1200/(spacing))+2):
            for y in range(math.floor(1200/(spacing))+2):
                pygame.draw.rect(screen, (200,200,200), (x*spacing + offset[0]%(spacing) - spacing,y*spacing + offset[1]%(spacing) - spacing, tile_size, tile_size))

    pygame.display.flip()
    mouse = pygame.mouse.get_pos()