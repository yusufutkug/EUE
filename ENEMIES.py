import random
import pygame as pg
from BULLET import *
from Sprites import*

class Enemy(Sprite):

    def __init__(self, pos,speed, all_sprites,bullets,enemies,screen,hero_bullets,wallet):
        super(Enemy, self).__init__(enemies,all_sprites)
        self.image = pg.Surface((32,64))
        self.image.fill((255,200,0))
        self.center=pos
        self.rect = self.image.get_rect(center=self.center)
        self.wallet=wallet
        self.health = 30
        self.speed=speed
        self.all_sprites=all_sprites
        self.bullets=bullets
        self.bullet_timer = 1.5
        self.bullet_time= 3
        self.damage = self.health
        self.vel=(0,120*int(speed**(1/2)))
        if self.vel[1]>=300:
                self.vel=(0,300)
        self.bullet_damage = 10
        self.bullet_health = 1 * int(speed**(1/2))
        self.bullet_image = pg.image.load("image\\bomb.png")
        self.score=0
        self.screen=screen
        self.dead=False
        self.current_animated = 0
        self.hero_bullets=hero_bullets
        self.animated = [pg.image.load("image\\Varlık 8.png"), pg.image.load("image\\Varlık 2.png"),
                    pg.image.load("image\\Varlık 4.png"), pg.image.load("image\\Varlık 9.png"),
                    pg.image.load("image\\Varlık 3.png"), pg.image.load("image\\Varlık 5.png"),
                    pg.image.load("image\\Varlık 6.png")]
        self.explosion=pg.mixer.Sound("sound\\explosion.wav")
        self.explosion.set_volume(0.5)
        self.coins=0
        self.x=0
        self.art=0.01
        self.contact=False
        
    def update(self, dt):
        if not self.dead:
            hits = self.spritecollide(self.hero_bullets,False)
            for bullet in hits:
                self.health=bullet.get_damage(self.health)
                bullet.change_health(self.damage)
            self.fire(dt,self.speed)
            if self.health <= 0:
                self.dead=True
                self.send_coin()
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


    def fire(self,dt,speed):
        self.bullet_timer -=dt
        if self.bullet_timer<=0:
            x=random.randint(0,1000)
            if x>=999-int((speed+0.6)**(1/2))//2:
                Bullet((self.rect.center[0],self.rect.center[1]+50), self.bullet_image,self.vel,self.bullet_damage, self.all_sprites, self.bullets,self.bullet_health)
                self.bullet_timer=self.bullet_time

    def move(self,x,y):

        self.rect.center=(self.center[0]+x,self.center[1]+y)
        if self.rect.right>=self.screen.get_width():
            self.contact=True
        elif self.rect.left<=0:
            self.contact=True   
        if self.rect.center[1]< 50:
            pass
        elif self.rect.center[1]> self.screen.get_height()-400:
            pass
        
  
    def Did_touch(self):
        if self.contact:
            self.contact=False
            return True
        else:
            return False

    def get_score_coin(self,score,coin) -> int:
        if self.dead:
            return (int(self.score)+score,int(self.coins)+coin)
        else:      
            return (score,coin)
    
    def send_coin(self):

        self.wallet.update_wallet(self.coins)

    def change_health(self,damage):
        
        self.health-=damage
    
    def get_damage(self,health):

        return health-self.health

    def get_pos(self):

        return self.rect.center

class Enemy1(Enemy):


    def __init__(self,pos, speed, all_sprites,bullets,enemies,screen,hero_bullets,wallet):
        super(Enemy1, self).__init__(pos, speed, all_sprites,bullets,enemies,screen,hero_bullets,wallet)
        self.image = pg.image.load("image\\enemy1.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 30*int(speed**(1/2))
        self.damage = self.health
        self.bullet_damage = 20*int(speed**(1/2))
        self.bullet_image = pg.image.load("image\\bomb.png")
        self.bullet_health = 12 * int(speed**(1/2))
        self.bullet_time = 3*(1/(int(speed**(1/2))))
        self.bullet_timer=3*(1/(int(speed**(1/2))))
        self.score = int(3*int(speed**(1/2)))
        self.coins=int(speed**(1/4))
        self.vel=(0,200*int(speed**(1/2)))
        if self.vel[1]>=400:
                self.vel=(0,400)


class Enemy2(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen,hero_bullets,wallet):
        super(Enemy2, self).__init__(pos, speed, all_sprites, bullets, enemies,screen,hero_bullets,wallet)
        self.image=pg.image.load("image\\enemy2.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 40*int(speed**(1/2))
        self.damage = self.health
        self.bullet_image = pg.image.load("image\\torpedo.png")
        self.bullet_damage = 25*int(speed**(1/2))
        self.bullet_health = 16 * int(speed**(1/2))
        self.bullet_time = 2*(1/int(speed**(1/2)))
        self.bullet_timer=2*(1/int(speed**(1/2)))
        self.score=int(7*int(speed**(1/2)))
        self.coins=int(2*int(speed**(1/4)))
        self.vel=(0,250*int(speed**(1/2)))
        if self.vel[1]>=450:
                self.vel=(0,450)


class Enemy3(Enemy):


    def __init__(self,pos,speed, all_sprites,bullets,enemies,screen,hero_bullets,wallet):
        super(Enemy3, self).__init__(pos,speed, all_sprites,bullets,enemies ,screen,hero_bullets,wallet)
        self.image=pg.image.load("image\\enemy3.png")
        self.rect = self.image.get_rect(center=pos)
        self.health = 50*int(speed**(1/2))
        self.damage = self.health
        self.bullet_damage = 30*int(speed**(1/2))
        self.bullet_image = pg.image.load("image\\nuclear-bomb.png")
        self.bullet_health=20*int(speed**(1/2))
        self.bullet_time = 1*(1/(int(speed**(1/2))))
        self.bullet_timer=1*(1/(int(speed**(1/2))))
        self.score=int(10*int(speed**(1/2)))
        self.coins=int(3*int(speed**(1/4)))
        self.vel=(0,300*int(speed**(1/2)))
        if self.vel[1]>=600:
                self.vel=(0,600)