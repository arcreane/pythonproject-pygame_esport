import pygame
pygame.init()
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_health = 10



class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.attack = 5




pygame.display.set_caption("Game")
window = pygame.display.set_mode((600,385))
window.fill((255,0,0))
background_image = pygame.image.load('images/background.png')

player = pygame.image.load('images/mario.gif')
playerPos = player.get_rect()
monster = pygame.image.load('images/gomba.png')
monsterPos = monster.get_rect()

monsterPos.x = 550
monsterPos.y = 275


playerPos.x = 0
playerPos.y = 230

run = True


while run:

    pygame.key.set_repeat(500, 30)
    window.blit(background_image, (0, 0))
    window.blit(player, (playerPos.x,playerPos.y))
    window.blit(monster, (monsterPos.x, monsterPos.y))
    pygame.display.flip()
    if playerPos.x == monsterPos.x and playerPos.y == 180:
        Monster.health = 0
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and playerPos.x < 500:
                playerPos.x += 10

            elif event.key == pygame.K_SPACE and playerPos.y > 0:
                playerPos.y -= 50

            elif event.key == pygame.K_LEFT and playerPos.x > 0:
                playerPos.x -= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerPos.y += 50