from random import randint, choice
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
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
            self.y += self.dy
            if self.y > 500:
                self.reset()

    def reset(self):
       self.x = choice(lanes)
       self.y = -64

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset() # this is where you call the reset.
    
    def move(self):
        self.x += self.dx
        if self.x > 500:
           self.reset()

    def reset(self):
       self.x = -64
       self.y = choice(lanes)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.lane_x_index = 1
        self.lane_y_index = 1
        # self.dx = 0
        # self.dy = 0
        self.reset()

    def left(self):
        if self.lane_x_index > 0:
            self.lane_x_index -= 1
            self.dx = lanes[self.lane_x_index]
            # self.dx -= 100
        
    def right(self):
        # if self.dx < 500 - 64:
        if self.lane_x_index < len(lanes) - 1:
            self.lane_x_index += 1
            self.dx = lanes[self.lane_x_index]
            # self.dx += 100

    def up(self):
        if self.lane_y_index > 0:
            self.lane_y_index -= 1
            self.dy = lanes[self.lane_y_index]
        # if self.dy > 0:
        #     self.dy  -= 100

    def down(self):
        # if self.dy < 500 -64:
        #     self.dy += 100
        if self.lane_y_index < len(lanes) - 1:
            self.lane_y_index += 1
            self.dy = lanes[self.lane_y_index]

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        self.x = max(0, min(self.x, 500 - 64))
        self.y = max(0, min(self.y, 500 - 64))

    def reset(self):
    #    self.x = 250 - 32
    #    self.y = 250 - 32
        self.lane_x_index = 1
        self.lane_y_index = 1
        self.dx = lanes[self.lane_x_index]
        self.dy = lanes[self.lane_y_index]
        self.x = self.dx
        self.y = self.dy

# example from 03-making-things-move
apple = Apple()
strawberry = Strawberry()
player = Player()
clock = pygame.time.Clock()

# game loop
running = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               running = False
            elif event.key == pygame.K_LEFT:
                player.left()
                print('LEFT')
            elif event.key == pygame.K_RIGHT:
                player.right()
                print('RIGHT')
            elif event.key == pygame.K_UP:
                player.up()
                print('UP')
            elif event.key == pygame.K_DOWN:
                player.down()
                print('DOWN')

    screen.fill((255, 255, 255))

    # draw apple
    apple.move()
    apple.render(screen)

    # draw strawberry
    strawberry.move()
    strawberry.render(screen)

    # draw player
    player.move()
    player.render(screen)

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
