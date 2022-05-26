import pygame as pg
from sympy import im


class Item(pg.sprite.Sprite):


    def __init__(self,speed,all_sprites,items_sprite,screen):
        super(Item, self).__init__(items_sprite)
        self.fee = 99999
        self.increase = 0
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.image=pg.image.load("label.png")
        self.rect=self.image.get_rect(topright=(screen.get_width(),100))
        self.name=None
        self.screen=screen
        self.font = pg.font.SysFont('ocraextended', 15)

    def get_increase(self):
        return self.increase

    def HowMuchisIt(self):
        return self.fee

    def update(self, dt) -> None:
        self.name_label=self.font.render(f"{self.name} {self.fee}$", True, (255, 255, 255))
        rect=self.name_label.get_rect(center=(self.rect.center))
        self.screen.blit(self.name_label,rect)



class Speed_of_Bullet(Item):


        def __init__(self,speed,all_sprites,items_sprite,screen):
            super(Speed_of_Bullet, self).__init__(speed,all_sprites,items_sprite,screen)
            self.fee = 65
            self.increase = 0.1
            self.image=pg.image.load("label1.png")
            self.rect=self.image.get_rect(topright=(screen.get_width(),70))
            self.name="Speed of Bullet"


class Shooting_Power(Item):


        def __init__(self,speed,all_sprites,items_sprite,screen):
            super(Shooting_Power, self).__init__(speed,all_sprites,items_sprite,screen)
            self.fee = 65
            self.increase = 5*int(speed**(1/2))
            self.image=pg.image.load("label1.png")
            self.rect=self.image.get_rect(topright=(screen.get_width(),144))
            self.name="Shooting Power"

