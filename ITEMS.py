import pygame as pg
from sympy import im
from Sprites import*


class Item(Sprite):


    def __init__(self,all_sprites,items_sprite,screen,game):
        super(Item, self).__init__(items_sprite,all_sprites)
        self.EUE=game
        self.fee = 99999
        self.increase = 0
        self.all_sprites=all_sprites
        self.image=pg.image.load("image\\label1.png")
        self.rect=self.image.get_rect(topright=(screen.get_width(),100))
        self.name=None
        self.screen=screen
        self.font = pg.font.SysFont('ocraextended', 15)
        self.font1 = pg.font.SysFont('ocraextended',15)
        self.canbebought=False

    def to_effect(self,hero):

        pg.mixer.Sound("sound\\mixkit-arcade-video-game-bonus-2044.wav").play()
        
    def trigger(self):
        if self.canbebought:
            objects=self.EUE.HereIsX(wallet=1,hero=1)
            objects[0].update_wallet(self.fee,-1)
            self.to_effect(objects[1])
            return True
        else:
            return False

    def Canbebought(self):
        objects=self.EUE.HereIsX(wallet=1)
        if objects[0].Am_I_Rich(self.fee):
            self.canbebought=True
        else:
            self.canbebought=False

    def update(self, dt) -> None:
        self.Canbebought()
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


        def __init__(self,speed,all_sprites,items_sprite,screen,game):
            super(Speed_of_Shooting, self).__init__(all_sprites,items_sprite,screen,game)
            self.fee = int(40*(speed**(1/2)))//10*10
            self.increase = 0.1
            self.rect=self.image.get_rect(topright=(screen.get_width(),70))
            self.name="Speed of Shooting"
            self.canbebought=False

        def to_effect(self,Hero):
             super().to_effect(Hero)
             Hero.change_bulletTime(self.increase)


class Shooting_Power(Item):


        def __init__(self,speed,all_sprites,items_sprite,screen,game):
            super(Shooting_Power, self).__init__(all_sprites,items_sprite,screen,game)
            self.fee = int(40*(speed**(1/2)))//10*10
            self.increase = int(5*int(speed**(1/4)))
            self.rect=self.image.get_rect(topright=(screen.get_width(),144))
            self.name="Shooting Power"
            self.effect="damage"
            self.canbebought=False
        
        def to_effect(self,Hero):
             super().to_effect(Hero)
             Hero.change_bulletDamage(self.increase)

