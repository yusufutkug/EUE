import pygame
screen=pygame.display.set_mode((200,200))
rect=pygame.Surface((20,30),10,fill=(255,0,0))

while True:
        screen.fill((255,255,255))
        screen.blit(rect,(50,50))
        pygame.display.flip()