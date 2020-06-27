import pygame
pygame.init()

monster = pygame.image.load('images/gomba.png')
monsterPos = monster.get_rect()

monsterPos.x = 550
monsterPos.y = 275
class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.attack = 5
