from random import randint
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

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # this is where you call the reset.
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500:
           self.reset()

    def reset(self):
       self.x = randint(50, 400)
       self.y = -64

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset() # this is where you call the reset.
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
           self.reset()

    def reset(self):
       self.x = -64
       self.y = randint(50, 400)


# instance of GameObject
screen.fill((255, 255, 255))

# example from 03-making-things-move
apple = Apple()
strawberry = Strawberry()
clock = pygame.time.Clock()

# game loop
running = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # apple.x += 1
    apple.move()
    strawberry.move()
    apple.render(screen)
    strawberry.render(screen)

    # apple1.render(screen)
    # apple2.render(screen)
    # apple3.render(screen)
    # apple4.render(screen)
    # apple5.render(screen)
    # strawberry1.render(screen)
    # strawberry2.render(screen)
    # strawberry3.render(screen)
    # strawberry4.render(screen)

    pygame.display.flip()
    clock.tick(60)
