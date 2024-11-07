# example 2

# initialize pygame
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

# game loop
running = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw a circle
    screen.fill((255, 255, 255))

    # update the window
    pygame.display.flip()

    surf = pygame.Surface ((50, 50))
    surf.fill((255, 111, 33))

    #  Clear screen
    screen.fill((255, 255, 255))

    # Draw the surface
    screen.blit(surf, (100, 120))

    pygame.display.flip()