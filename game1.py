import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

color = (105, 105, 105)

radius = 70
padding = 25
rows = 3
cols = 3

#the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #clear the screen
    screen.fill((255, 255, 255))

    # challenge 1
    # draw a circle

    # #red
    # color = (255, 0, 0) 
    # position = (100, 100)
    # pygame.draw.circle(screen, color, position, 75)

    # #orange
    # color = (255, 165, 0)
    # position = (400, 100)
    # pygame.draw.circle(screen, color, position, 75)

    # #yellow
    # color = (255, 255, 0)
    # position = (250, 250)
    # pygame.draw.circle(screen, color, position, 75)

    # #green
    # color = (0, 255, 0)
    # position = (100, 400)
    # pygame.draw.circle(screen, color, position, 75)

    # #cyan
    # color = (0, 255, 255)
    # position = (400, 400)
    # pygame.draw.circle(screen, color, position, 75)


    # challenge 2

    for row in range(rows):
        for col in range(cols):
            x = col * (2 * radius + padding) + radius + padding // 2
            y = row * (2 * radius + padding) + radius + padding // 2
            position = (x, y)
            

            pygame.draw.circle(screen, color, position, radius)



    #update the display
    pygame.display.flip()


