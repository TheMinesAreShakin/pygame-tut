#import pygame
import pygame

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


def render():
    screen.fill((0, 0, 0))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


#initialize all the pygame modules
pygame.init()

#consts for w and h
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create screan object
#screen is a surface that represents the inside dimensions of the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

#game loop var
running = True

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

    render()