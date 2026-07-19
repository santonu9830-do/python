import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

background_image = pygame.transform.scale(pygame.image.load("white bg.jpg").convert(), (400, 500))

PENGUIN_IMAGE = pygame.transform.scale(pygame.image.load("penguin.jpg").convert_alpha(), (200, 200))
penguin_rect = PENGUIN_IMAGE.get_rect(center=(400 // 2, 500 // 2))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            

    
    screen.blit(background_image, (0, 0))
    screen.blit(PENGUIN_IMAGE, penguin_rect)
    pygame.display.flip()