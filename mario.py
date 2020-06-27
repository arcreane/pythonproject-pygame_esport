import pygame
pygame.init()

player = pygame.image.load('images/mario.gif')
playerPos = player.get_rect()
playerPos.x = 0
playerPos.y = 230
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_health = 10