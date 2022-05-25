import pygame
import sys

pygame.init()

pencere = pygame.display.set_mode((200,200), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT and pygame.K_RETURN :
                print("ıuu")
                pygame.display.toggle_fullscreen

    pygame.display.flip()