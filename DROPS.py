import pygame as pg


class Drops(pg.sprite.Sprite):


    def __init__(self,pos,all_sprites,drop_sprite,hero_bullets,screen,firex) -> None:
        super(Drops,self).__init__(drop_sprite)
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.hero_bullets=hero_bullets
        self.image=pg.Surface((20,30),10)
        self.image.fill((255,0,0))
        self.center=pos
        self.rect=self.image.get_rect(center=self.center)
        self.x=0
        self.screen=screen
        self.screenWidth=self.screen.get_width()
        self.health=firex
        self.effect=0
        self.me="pass"
        
    
    def update(self,dt):
        hero_bullet=pg.sprite.spritecollide(self,self.hero_bullets,True)
        for i in hero_bullet:
            self.health-=1
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
    
    def get_effect(self):
        return [self.me, self.effect]


    
class Power_Upp(Drops):


    def __init__(self, pos, all_sprites, drop_sprite,hero_bullets,screen,firex) -> None:
        super(Power_Upp,self).__init__(pos, all_sprites, drop_sprite,hero_bullets,screen,firex)
        self.image=pg.image.load("image\\ammo.png")
        self.effect=1
        self.me="power"


class Health_Upp(Drops):


    def __init__(self, pos, all_sprites, drop_sprite,hero_bullets, screen,firex) -> None:
        super().__init__(pos, all_sprites, drop_sprite,hero_bullets, screen,firex)
        self.image=pg.image.load("image\\gear.png")
        self.effect=15
        self.me="health"


