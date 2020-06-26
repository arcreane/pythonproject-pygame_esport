import pygame
pygame.init()


pygame.display.set_caption("Game")
window = pygame.display.set_mode((600,385))
window.fill((255,0,0))
background_image = pygame.image.load('images/background.png')


run = True


while run:

    window.blit(background_image, (0, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("test")