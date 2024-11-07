# example 2

# initialize pygame
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

# box = GameObject(120, 300, 50, 50)

# instance of GameObject
screen.fill((255, 255, 255))

# apple 1 & strawberry 1 & apple 2
apple1 = GameObject(100, 100, 'apple.png')
strawberry1 = GameObject(225, 100, 'strawberry.png')
apple2 = GameObject(350, 100, 'apple.png')

# strawberry 2 apple 3 & strawberry 3
strawberry2 = GameObject(100, 225, 'strawberry.png')
apple3 = GameObject(225, 225, 'apple.png')
strawberry3 = GameObject(350, 225, 'strawberry.png')


# apple 4 & strawberry 4 & apple 5
apple4 = GameObject(100, 350, 'apple.png')
strawberry4 = GameObject(225, 350, 'strawberry.png')
apple5 = GameObject(350, 350, 'apple.png')

# game loop
running = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    apple1.render(screen)
    apple2.render(screen)
    apple3.render(screen)
    apple4.render(screen)
    apple5.render(screen)
    strawberry1.render(screen)
    strawberry2.render(screen)
    strawberry3.render(screen)
    strawberry4.render(screen)

    pygame.display.flip()

