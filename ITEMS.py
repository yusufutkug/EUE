import pygame as pg
from sympy import im


class Item(pg.sprite.Sprite):


    def __init__(self,speed,all_sprites,items_sprite,screen):
        super(Item, self).__init__(items_sprite)
        self.fee = 99999
        self.increase = 0
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.image=pg.image.load("image\\label1.png")
        self.rect=self.image.get_rect(topright=(screen.get_width(),100))
        self.name=None
        self.screen=screen
        self.font = pg.font.SysFont('ocraextended', 15)
        self.font1 = pg.font.SysFont('ocraextended',15)
        self.canbebought=False

    def get_increase(self):
        pg.mixer.Sound("sound\\mixkit-arcade-video-game-bonus-2044.wav")
        return self.increase

    def HowMuchisIt(self):
        return self.fee

    def Canbebought(self,coins):
        if coins>=self.fee:
            self.canbebought=True
        else:
            self.canbebought=False

    def update(self, dt) -> None:
        if self.canbebought:
            self.name_label=self.font.render(f"{self.name} {self.fee}$", True, (0,255,0))
            self.effect_label=self.font1.render(f" +{self.increase}",True, (0,255,0))
        else:
            self.name_label=self.font.render(f"{self.name} {self.fee}$", True, (255,0,0))
            self.effect_label=self.font1.render(f" +{self.increase}",True, (255,0,0))
        rect=self.name_label.get_rect(center=(self.rect.center))
        rect1=self.effect_label.get_rect(topleft=(rect.bottomleft))
        self.screen.blit(self.name_label,rect)
        self.screen.blit(self.effect_label,rect1)

    



class Speed_of_Shooting(Item):


        def __init__(self,speed,all_sprites,items_sprite,screen):
            super(Speed_of_Shooting, self).__init__(speed,all_sprites,items_sprite,screen)
            self.fee = int(40*(speed**(1/2)))//10*10
            self.increase = 0.1
            self.rect=self.image.get_rect(topright=(screen.get_width(),70))
            self.name="Speed of Shooting"
            self.canbebought=False



class Shooting_Power(Item):


        def __init__(self,speed,all_sprites,items_sprite,screen):
            super(Shooting_Power, self).__init__(speed,all_sprites,items_sprite,screen)
            self.fee = int(40*(speed**(1/2)))//10*10
            self.increase = int(5*int(speed**(1/4)))
            self.rect=self.image.get_rect(topright=(screen.get_width(),144))
            print(screen.get_width())
            self.name="Shooting Power"
            self.effect="damage"
            self.canbebought=False

