import random
import pygame as pg
from BULLET import *

class Enemy(pg.sprite.Sprite):

    def __init__(self, pos,speed, all_sprites,bullets,enemies,screen):
        super(Enemy, self).__init__(enemies)
        self.image = pg.image.load("enemy1.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 30
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.bullets=bullets
        self.bullet_timer = 3
        self.bullet_time= 3
        self.damage = self.health
        self.vel=(0,60*int(speed))
        if self.vel[1]>=300:
                self.vel=(0,300)
        self.bullet_damage = 10
        self.bullet_health = 1 * (speed)
        self.bullet_image = pg.image.load("bomb.png")
        self.score=0
        self.screen=screen
        self.dead=False
        self.current_animated = 0
        self.animated = [pg.image.load("Varlık 8.png"), pg.image.load("Varlık 2.png"),
                    pg.image.load("Varlık 4.png"), pg.image.load("Varlık 9.png"),
                    pg.image.load("Varlık 3.png"), pg.image.load("Varlık 5.png"),
                    pg.image.load("Varlık 6.png")]
        self.explosion=pg.mixer.Sound("explosion.wav")

    def update(self, dt):
        if not self.dead:
            self.fire(dt)
            if self.health <= 0:
                self.dead=True
                self.explosion.play()

        else:
            self.animation()
            

    def animation(self):

        self.image=self.animated[int(self.current_animated)]
        self.current_animated+=0.25
        if self.current_animated>=len(self.animated):
            self.current_animated=0
            self.kill()

        rect=self.image.get_rect(center=(self.rect.center))
        self.screen.blit(self.image,rect)


    def fire(self,dt):
        self.bullet_timer -=dt
        if self.bullet_timer<=0:
            x=random.randint(0,1000)
            if x>999:
                Bullet((self.rect.center[0],self.rect.center[1]+50), self.bullet_image,self.vel,self.bullet_damage, self.all_sprites, self.bullets,self.bullet_health)
                self.bullet_timer=self.bullet_time
    def move_down_up(self,direction):
        pass
    def move_right_left(self,direction):
        pass

class Enemy1(Enemy):


    def __init__(self,pos, speed, all_sprites,bullets,enemies,screen):
        super(Enemy1, self).__init__(pos, speed, all_sprites,bullets,enemies,screen)
        self.image = pg.image.load("enemy1.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 30*(speed)
        self.damage = self.health
        self.bullet_damage = 10*(speed)
        self.bullet_image = pg.image.load("bomb.png")
        self.bullet_health = 12 * (speed)
        self.bullet_time = 3*(1/((speed)))
        self.score = int(3*(speed))


class Enemy2(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen):
        super(Enemy2, self).__init__(pos, speed, all_sprites, bullets, enemies,screen)
        self.image=pg.image.load("enemy2.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 40*(speed)
        self.damage = self.health
        self.bullet_image = pg.image.load("torpedo.png")
        self.bullet_damage = 15*(speed)
        self.bullet_health = 16 * (speed)
        self.bullet_time = 1*(1/((speed)))
        self.score=int(7*(0.6+speed))


class Enemy3(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen):
        super(Enemy3, self).__init__(pos,speed, all_sprites,bullets,enemies ,screen)
        self.image=pg.image.load("enemy3.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 50*(speed)
        self.damage = self.health
        self.bullet_damage = 20*(speed)
        self.bullet_image = pg.image.load("nuclear-bomb.png")
        self.bullet_health=20*(speed)
        self.bullet_time = 1*(1/((speed)))
        self.score=int(10*(speed))