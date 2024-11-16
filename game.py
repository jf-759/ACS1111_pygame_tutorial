import pygame # type: ignore
pygame.init()
from random import randint, choice

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

background = pygame.image.load('sky.png')
background = pygame.transform.scale(background, (screen_width, screen_height))


lanes = [93, 218, 343]
capture = 0
initial_speed = 1
increase_speed = 0.2

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image) # ADD!
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect() # this will give each image a dimension around it (to eventually get to collisions).

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Pizza(GameObject):
    def __init__(self):
        super(Pizza, self).__init__(0, 0, 'pizza.png')
        self.surf = pygame.transform.scale(self.surf, (64, 64))
        self.dx = 0
        self.dy = initial_speed
        self.direction = 'down'
        self.reset() # this is where you call the reset.
    
    def move(self):
            if self.direction == 'down':
                self.y += self.dy
                if self.y > 500:
                    self.reset()

            elif self.direction == 'up':
                self.y -= self.dy
                if self.y < -64:
                    self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64
        self.direction = choice(['up', 'down'])
        # speed = (randint(0, 200) / 100)
        if self.direction == 'down':
            self.y = -64
            self.dy = initial_speed + (capture * increase_speed)

        elif self.direction == 'up':
            self.y = 500
            self.dy = initial_speed + (capture * increase_speed)


class Chicken(GameObject):
    def __init__(self):
        super(Chicken, self).__init__(0, 0, 'fried_chicken.png')
        self.surf = pygame.transform.scale(self.surf, (64, 64))
        self.dx = initial_speed
        self.dy = 0
        self.direction = 'right'
        self.reset() # this is where you call the reset.
    
    def move(self):
        if self.direction == 'right':
            self.x += self.dx
            if self.x > 500:
                self.reset()

        elif self.direction == 'left':
            self.x -= self.dx
            if self.x < -64:
                self.reset()

    def reset(self):
        self.y = choice(lanes)
        self.direction = choice(['left', 'right'])
        speed = (randint(0, 200) / 100)
        if self.direction == 'right':
            self.x = -64 if choice([True, False]) else 500
            self.dx = initial_speed + (capture * increase_speed)
        elif self.direction == 'left':
            self.x = 500 
            self.dx = initial_speed + (capture * increase_speed)

class Rock(GameObject):
    def __init__(self):
        super(Rock, self).__init__(0, 0, 'rocks-1.png')
        self.surf = pygame.transform.scale(self.surf, (64, 64))
        self.dx = 0
        self.dy = 0
        self.direction = choice(['up', 'down', 'left', 'right'])
        self.reset()

    def move(self):
        if self.direction == 'down':
            self.y += self.dy
            if self.y > 500:
                self.reset()
        elif self.direction =='up':
            self.y -= self.dy
            if self.y < -64:
                self.reset()

        elif self.direction == 'right':
            self.x += self.dx
            if self.x > 500:
                self.reset()
        elif self.direction == 'left':
            self.x -= self.dx
            if self.x < -64:
                self.reset()
    
    def reset(self):
        self.direction = choice(['up', 'down', 'left', 'right'])
        speed = (randint (50, 100) / 100)
        if self.direction == 'down':
            self.x = choice(lanes)
            self.y = -64
            self.dy = speed + 1
            self.dx = 0
        
        elif self.direction == 'up':
            self.x = choice(lanes)
            self.y = 500
            self.dy = speed + 1
            self.dx = 0
        
        elif self.direction == 'right':
            self.x = -64
            self.y = choice(lanes)
            self.dx = speed + 1
            self.dy = 0

        elif self.direction == 'left':
            self.x = 500
            self.y = choice(lanes)
            self.dx = speed + 1
            self.dy = 0

class Cloud(GameObject):
    def __init__(self):
        cloud_images = ['Cloud-a.png', 'Cloud-b.png', 'Cloud-c.png']
        cloud_image = choice(cloud_images)

        super(Cloud, self).__init__(-64, randint(0, screen_height //2),  cloud_image)
        # self.surf = pygame.transform.scale(self.surf, (randint(64, 128), randint(32, 64)))
        self.dx = randint(1, 3) # this is for the cloud's speed

    def move(self):
        self.x += self.dx
        if self.x > screen_width: # resets when cloud goes off screen
            self.reset()

    def reset(self):
        cloud_images = ['Cloud-a.png', 'Cloud-b.png', 'Cloud-c.png']
        cloud_image = choice(cloud_images)
        self.surf = pygame.image.load(cloud_image)
        
        self.x = -64
        self.y = randint(0, screen_height // 2)
        self.dx = randint(1, 3)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'w.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1 # new attribute
        self.pos_y = 1 # new attribute
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()
            # self.dx -= 100
        
    def right(self):
        # if self.dx < 500 - 64:
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()
            # self.dx += 100

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()
        # if self.dy > 0:
        #     self.dy  -= 100

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        self.x = max(0, min(self.x, 500 - 64))
        self.y = max(0, min(self.y, 500 - 64))

    def reset(self):
        self.x = choice(lanes)
        self.y = -64
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.x = self.dx
        self.y = self.dy

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]
    
def reset_game():
    global capture
    capture = 0
    player.reset()
    pizza.reset()
    chicken.reset()
    rock.reset()

# example from 03-making-things-move
pizza = Pizza()
chicken = Chicken()
player = Player()
rock = Rock()
cloud = Cloud()

all_sprites = pygame.sprite.Group()
food_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()

all_sprites.add(player)
all_sprites.add(pizza)
all_sprites.add(chicken)
all_sprites.add(rock)
all_sprites.add(cloud)

food_sprites.add(pizza)
food_sprites.add(chicken)



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


    # move and render Sprites
    for entity in all_sprites:
        entity.move()

    food = pygame.sprite.spritecollideany(player, food_sprites)
    if food:
        capture += 1
        food.reset()

    if pygame.sprite.collide_rect(player, rock):
        reset_game()

    screen.blit(background, (0, 0))
    for entity in all_sprites:
        entity.render(screen)

    pygame.display.flip()
    clock.tick(60)
