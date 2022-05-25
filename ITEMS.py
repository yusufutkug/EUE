import pygame as pg


class Item(pg.sprite.Sprite):


    def __init__(self,speed,items_sprite):
        super(Item, self).__init__(items_sprite)
        self.fee = 99999
        self.increase = 0
        self.

    def get_increase(self):
        return self.increase

    def HowMuchisIt(self):
        return self.fee

    def update(self, dt) -> None:



class Speed_of_Bullet(Item):


        def __init__(self):
            super(Speed_of_Bullet, self).__init__()
            self.fee = 99999
            self.increase = 0.1z


class Shooting_Power(Item):


        def __init__(self,):
            super(Shooting_Power, self).__init__()
            self.fee = ((50*k)//10)*10
            self.increase = 5

