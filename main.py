import pygame
from mario import *
from monster import *
from block import *
pygame.init()
pygame.key.set_repeat(500, 30)

pygame.display.set_caption("Game")
window = pygame.display.set_mode((600,385))
window.fill((255,0,0))
background_image = pygame.image.load('images/background.png')







run = True


while run:


    window.blit(background_image, (0, 0))
    window.blit(player, (playerPos.x,playerPos.y))
    window.blit(monster, (monsterPos.x, monsterPos.y))
    window.blit(block, (blockPos.x, blockPos.y))
    pygame.display.flip()
    if playerPos.x == monsterPos.x and playerPos.y == 180:
        Monster.health = 0
    elif monsterPos.x != playerPos.x :
        monsterPos.x -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and playerPos.x < 500:
                if playerPos.x < blockPos.x - 75 and playerPos.y < blockPos.y:
                    playerPos.x += 10

            elif event.key == pygame.K_SPACE and playerPos.y > 0:
                playerPos.y -= 100

            elif event.key == pygame.K_LEFT and playerPos.x > 0:
                playerPos.x -= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerPos.y += 100