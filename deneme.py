
import pygame as pg
screen=pg.display.set_mode((500,300))
animated=[pg.Surface((1,screen.get_height())),pg.Surface((1,screen.get_height())),pg.Surface((1,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((1,screen.get_height()))]
current_animated=0
while True:
        mouse_pressed = pg.mouse.get_pressed()
        image=animated[int(current_animated)]
        image.fill((255,0,0))
        current_animated+=0.007
    
        if current_animated>=len(animated):
            current_animated=0
        screen.fill((0,0,0))
        rect=image.get_rect(midbottom=(250,150))
        print(rect.w)
        screen.blit(image,rect)
        pg.display.flip()
