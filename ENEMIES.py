import random
import math
import pygame as pg
from BULLET import *

class Enemy(pg.sprite.Sprite):

    def __init__(self, pos,speed, all_sprites,bullets,enemies,screen,hero_bullets):
        super(Enemy, self).__init__(enemies)
        self.image = pg.image.load("enemy1.png")
        self.center=pos
        self.rect = self.image.get_rect(center=self.center)
        self.health = 30
        self.speed=speed
        self.all_sprites=all_sprites
        self.add(self.all_sprites)
        self.bullets=bullets
        self.bullet_timer = 3
        self.bullet_time= 3
        self.damage = self.health
        self.vel=(0,80*int(speed**(1/2)))
        if self.vel[1]>=300:
                self.vel=(0,300)
        self.bullet_damage = 10
        self.bullet_health = 1 * int(speed**(1/2))
        self.bullet_image = pg.image.load("bomb.png")
        self.score=5
        self.screen=screen
        self.dead=False
        self.current_animated = 0
        self.hero_bullets=hero_bullets
        self.animated = [pg.image.load("Varlık 8.png"), pg.image.load("Varlık 2.png"),
                    pg.image.load("Varlık 4.png"), pg.image.load("Varlık 9.png"),
                    pg.image.load("Varlık 3.png"), pg.image.load("Varlık 5.png"),
                    pg.image.load("Varlık 6.png")]
        self.explosion=pg.mixer.Sound("explosion.wav")
        self.coins=0
        self.x=0
        self.art=0.01
        
        
        

    def update(self, dt):
        if not self.dead:
            hits = pg.sprite.spritecollide(self, self.hero_bullets,True)
            for bullet in hits:
                self.health-=bullet.get_damage()
            self.fire(dt,self.speed)
            if self.health <= 0:
                self.dead=True
                self.explosion.play()
            self.move()
       
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


    def fire(self,dt,speed):
        self.bullet_timer -=dt
        if self.bullet_timer<=0:
            x=random.randint(0,1000)
            if x>999-int((speed+0.6)**(1/2))//2:
                Bullet((self.rect.center[0],self.rect.center[1]+50), self.bullet_image,self.vel,self.bullet_damage, self.all_sprites, self.bullets,self.bullet_health)
                self.bullet_timer=self.bullet_time

    def move(self):

        #self.rect.centery=self.center[1]
        #self.rect.centerx=self.center[0]
        
        x=self.x
        y=50*math.sin(x)
        self.rect.center=(self.center[0]+5*x,self.center[1]-y)
        if self.rect.center[0]>=self.screen.get_width()-200:
           self.art=-0.01
        elif self.rect.center[0]<=200:
            self.art=0.01
        if self.rect.center[1]< 50:
            pass
        elif self.rect.center[1]> self.screen.get_height()-400:
            pass
        self.x+=self.art
  
        

    def get_score_coin(self) -> int:
        if self.dead:
            return (int(self.score),int(self.coins))
        else:
            return (0,0)
    
    def get_damage(self):

        return self.health

    def get_pos(self):

        return self.rect.center

class Enemy1(Enemy):


    def __init__(self,pos, speed, all_sprites,bullets,enemies,screen,hero_bullets):
        super(Enemy1, self).__init__(pos, speed, all_sprites,bullets,enemies,screen,hero_bullets)
        self.image = pg.image.load("enemy1.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 30*int(speed**(1/2))
        self.damage = self.health
        self.bullet_damage = 10*int(speed**(1/2))
        self.bullet_image = pg.image.load("bomb.png")
        self.bullet_health = 12 * int(speed**(1/2))
        self.bullet_time = 3*(1/(int(speed**(1/2))))
        self.score = int(3*int(speed**(1/2)))
        self.coins=int(speed**(1/4))


class Enemy2(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen,hero_bullets):
        super(Enemy2, self).__init__(pos, speed, all_sprites, bullets, enemies,screen,hero_bullets)
        self.image=pg.image.load("enemy2.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 40*int(speed**(1/2))
        self.damage = self.health
        self.bullet_image = pg.image.load("torpedo.png")
        self.bullet_damage = 15*int(speed**(1/2))
        self.bullet_health = 16 * int(speed**(1/2))
        self.bullet_time = 1*(1/int(speed**(1/2)))
        self.score=int(7*int(speed**(1/2)))
        self.coins=int(2*int(speed**(1/4)))


class Enemy3(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen,hero_bullets):
        super(Enemy3, self).__init__(pos,speed, all_sprites,bullets,enemies ,screen,hero_bullets)
        self.image=pg.image.load("enemy3.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 50*int(speed**(1/2))
        self.damage = self.health
        self.bullet_damage = 20*int(speed**(1/2))
        self.bullet_image = pg.image.load("nuclear-bomb.png")
        self.bullet_health=20*int(speed**(1/2))
        self.bullet_time = 1*(1/(int(speed**(1/2))))
        self.score=int(10*int(speed**(1/2)))
        self.coins=int(3*int(speed**(1/4)))