import pygame as pg
from Sprites import*


class Drops(Sprite):


    def __init__(self,Health,screen,all_sprites,heroSprite,drop_sprite,hero_bullets) -> None:
        super(Drops,self).__init__(drop_sprite,all_sprites)
        self.center=(-1000,-1000)
        self.hero_bullets=hero_bullets
        self.hero=heroSprite
        self.image=pg.Surface((20,30),10)
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect(center=self.center)
        self.x=0
        self.screen=screen
        self.screenWidth=self.screen.get_width()
        self.health=Health
        self.effect=0
        self.dropsound=pg.mixer.Sound("sound\\water_drop-6707.wav")
        
        

    def update(self,dt):
        hero_bullet=self.spritecollide(self.hero_bullets)
        for i in hero_bullet:
            self.health-=1
        drop_Hero=self.spritecollide(self.hero)
        if len(drop_Hero)==1:
                self.to_effect(drop_Hero[0])
        if self.health<=0:
            self.kill()
        x=self.x
        if self.screenWidth//2<self.center[0]:
            y=int((1/200)*self.x**3-7*self.x)
            self.rect.center=(self.center[0]+2*x,self.center[1]-y)
            self.x-=0.3
            self.screenWidth=0
        else:
            y=int(-((1/200)*self.x**3-7*self.x))
            self.rect.center=(self.center[0]+2*x,self.center[1]-y)
            self.x+=0.3
            self.screenWidth=9999
        if self.center[1]-y>self.screen.get_height():
            self.kill()

    def to_effect(self,hero):

        self.kill()

    def change_center(self,center):

        self.center=center
    
class Power_Upp(Drops):


    def __init__(self, all_sprites, drop_sprite,hero_bullets,screen,firex,heroSprite) -> None:
        super(Power_Upp,self).__init__( all_sprites, drop_sprite,hero_bullets,screen,firex,heroSprite)
        self.image=pg.image.load("image\\ammo.png")
        self.effect=1
    
    def to_effect(self,hero):
        self.dropsound.play()
        hero.change_Firex()
        self.kill()


class Health_Upp(Drops):


    def __init__(self, all_sprites, drop_sprite,hero_bullets, screen,firex,heroSprite) -> None:
        super().__init__( all_sprites, drop_sprite,hero_bullets, screen,firex,heroSprite)
        self.image=pg.image.load("image\\gear.png")
        self.effect=15

    def to_effect(self,hero):
        self.dropsound.play()
        hero.change_health(self.effect,1)
        self.kill()
