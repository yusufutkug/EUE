import pygame as pg
from Sprites import*

class Bullet(Sprite):


    def __init__(self, pos,img,vel,dam, all_sprites,enemy,bullets,health=1):
        super().__init__(bullets,all_sprites)
        self.enemy=enemy
        self.image = img
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pg.math.Vector2(pos)
        self.vel = pg.math.Vector2(vel)
        self.damage = dam
        self.health=health

    def update(self, dt):
        hit=self.spritecollide(self.enemy)
        for enemy in hit:
            self.send_damage(enemy)
        self.pos += self.vel * dt
        self.rect.midbottom = self.pos  
        if self.rect.top <= 0 or self.health<=0:
            self.kill()


    def send_damage(self,enemy):

        enemy.change_health(self.damage)

    def change_health(self,damage):

        self.health-=damage

