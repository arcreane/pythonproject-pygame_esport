import pygame
pygame.init()

block = pygame.image.load('images/block.png')
blockPos = block.get_rect()

blockPos.x = 200
blockPos.y = 225