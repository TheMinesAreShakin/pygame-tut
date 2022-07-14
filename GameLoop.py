#import pygame
import pygame
import random

#Importing pygame.locals move the namespace of the constants
#to the global namespace instead of the pygame namespace so
#that you can use K_LEFT instead of pygame.K_LEFT
#alternate import to get all consts: from pygame.locals import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class Player(pygame.sprite.Sprite):


    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


    def update(self, pressedKeys):
        if pressedKeys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressedKeys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressedKeys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressedKeys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):


    def __init__(self):
        super(Enemy, self).__init__(self)
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            #.kill removes the sprite from every group to which it belongs
            self.kill()


def render():
    #fill background to prevent it from being a drawing game
    screen.fill((0, 0, 0))

    #blit each sprite to the screen surface using the allSprites group
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)

    #update the display
    pygame.display.flip()


def update():
    pressedKeys = pygame.key.get_pressed()
    player.update(pressedKeys)

    # update is a method on the Sprite group that calls the update
    # method for all members of the group
    enemies.update()

def add_enemy():
    new_enemy = Enemy()
    enemies.add(new_enemy)
    allSprites.add(new_enemy)


#initialize all the pygame modules
pygame.init()

#consts for w and h
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create screan object
#screen is a surface that represents the inside dimensions of the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#create custom event to add new enemy (first line described in notes)
EVENT_ADD_ENEMY = pygame.USEREVENT + 1
#set timer takes an event to repeat on an interval in miliseconds
# in this case it will trigger EVENT_ADD_ENEMY every 250 ms
pygame.time.set_timer(EVENT_ADD_ENEMY, 250)

#create player
player = Player()

#create sprite groups
enemies = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(player)

#game loop var
running = True

clock = pygame.time.Clock()

#game loop
while running:
    #look at every event in the event queue
    for event in pygame.event.get():
        #did the user hit a key?
        if event.type == KEYDOWN:
            #was it escape?
            if event.key == K_ESCAPE:
                running = False
        
        #did the user click the close button?
        elif event.type == QUIT:
            running = False

        # enemy event handler
        elif event.type == EVENT_ADD_ENEMY:
            add_enemy()

    update()
    render()

    clock.tick(60)