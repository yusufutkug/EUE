import pygame as pg

class Bullet(pg.sprite.Sprite):


    def __init__(self, pos,img,vel,dam, all_sprites,bullets,health=1):
        super().__init__(bullets)
        self.image = img
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pg.math.Vector2(pos)
        self.vel = pg.math.Vector2(vel)
        self.damage = dam
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.health=health

    def update(self, dt):
        self.pos += self.vel * dt
        self.rect.midbottom = self.pos  
        if self.rect.top <= 0 or self.health<=0:
            self.kill()
    def get_damage(self):

        return self.damage
    
    def change_health(self,damage):
        self.health-=damage

