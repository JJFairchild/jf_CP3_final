import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1200, 1200))

tile_size = 100
spacing = tile_size*9/8
offset = [0,0]
first_frame = True
drag = False
scroll = False
mouse = pygame.mouse.get_pos()


def stow(pos):
    pos = ((mouse[0]+offset[0])/(spacing), (mouse[1]+offset[1])/(spacing))
    return (math.floor(pos[0]), math.floor(pos[1]))

running = True
while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(stow(mouse))
            if event.button == 3:
                drag = True

        if event.type == pygame.MOUSEWHEEL:
            scroll = True
            if event.y > 0:
                tile_size *= 9/8
                spacing = tile_size*9/8
            elif event.y < 0:
                tile_size /= 9/8
                spacing = tile_size*9/8

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            drag = False

    new_mouse = pygame.mouse.get_pos()
    if (drag and mouse != new_mouse) or first_frame or scroll:
        # Drag movement
        offset[0] += (mouse[0] - new_mouse[0])
        offset[1] += (mouse[1] - new_mouse[1])
        mouse = new_mouse

        scroll = False
        print(offset)
        

        # Draw screen
        screen.fill((50,50,50))
        for x in range(math.floor(1200/(spacing))+2):
            for y in range(math.floor(1200/(spacing))+2):
                pygame.draw.rect(screen, (200,200,200), (x*spacing - offset[0]%spacing, y*spacing - offset[1]%spacing, tile_size, tile_size))

    pygame.display.flip()
    mouse = pygame.mouse.get_pos()
    first_frame = False