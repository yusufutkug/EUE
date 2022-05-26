import pygame as pg

class Bullet(pg.sprite.Sprite):


    def __init__(self, pos,img,vel,dam, all_sprites,bullets,health=200):
        super().__init__(bullets)
        self.image = img
        self.rect = self.image.get_rect(center=pos)
        self.pos = pg.math.Vector2(pos)
        self.vel = pg.math.Vector2(vel)
        self.damage = dam
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.health=health

    def update(self, dt):
        # Add the velocity to the position vector to move the sprite.
        self.pos += self.vel * dt
        self.rect.center = self.pos  # Update the rect pos.
        if self.rect.bottom <= 0 or self.health<=0:
            self.kill()
    def get_damage(self):
        return self.damage

