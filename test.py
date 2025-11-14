import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 1200))

tile_size = 100
mouse = pygame.mouse.get_pos()

running = True
while running:

    # Events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            running = False
        
        
        if pygame.mouse.get_pressed()[0]:
            print(f"Left mouse button clicked at {mouse}")

    #print(mouse)

    """
    if mouse != pygame.mouse.get_pos():
        for x in range(int(1200/(tile_size*9/8))+1):
            for y in range(int(1200/(tile_size*9/8))+1):
                pygame.draw.rect(screen, (200,200,200), (x*tile_size*9/8,y*tile_size*9/8, tile_size, tile_size))
    """
    
    pygame.display.flip()
    mouse = pygame.mouse.get_pos()