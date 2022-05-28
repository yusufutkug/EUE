from re import S
from ssl import enum_certificates
import pygame as pg
from BULLET import *
class Heros(pg.sprite.Sprite):


    def __init__(self, pos,window, all_sprites, bullets,sprite_groups,enemy_bullets,enemies,drops):
        super(Heros, self).__init__(sprite_groups)
        self.hero_death=False
        self.cor=pos
        self.image_list=[pg.image.load("image\\hr1.png"),pg.image.load("image\\hr4.png"),pg.image.load("image\\hr1.png"), pg.image.load("image\\hr2.png"), pg.image.load("image\\hr3.png"), pg.image.load("image\\hr2.png"), pg.image.load("image\\hr1.png")]
        self.current_image=0
        self.image = self.image_list[self.current_image]
        self.rect = self.image.get_rect(center=self.cor)
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets
        self.enemy_bullets=enemy_bullets
        self.enemies=enemies
        self.drops=drops
        self.bullet_timer = 1
        self.bullet_time=0.1
        self.bullet_img=pg.Surface((3,10))
        self.bullet_img.fill((255,0,0))
        self.health=100
        self.max_health=100
        self.screen=window
        self.bullet_damage=15
        self.bullet_vel=(0,-300)
        self.current_animated=0
        self.animated=[pg.image.load("image\\Untitled (1).png"),pg.image.load("image\\Untitled (2).png"),pg.image.load("image\\Untitled (3).png")]
        self.atackSkill=False
        self.defenseSkill=False
        self.laser_sound = pg.mixer.Sound('sound\\laser.wav')
        self.laser_sound.set_volume(0.3)
        self.amIGhost=False
        self.firex=1

    def move(self):
        self.cor=pg.mouse.get_pos()
        self.rect.center = self.cor

    def fire(self,dt,cor,x):
        mouse_pressed = pg.mouse.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if x%2==1:
               if mouse_pressed[0]:  # Left mouse button.
                        # Create a new bullet instance and add it to the groups.
                        Bullet(cor, self.bullet_img,self.bullet_vel,self.bullet_damage, self.all_sprites, self.bullets)
                        self.laser_sound.play()
                        if not x==1:
                            self.fire(dt,cor,(x-1))
                        else:
                            self.bullet_timer = self.bullet_time
            else:
                distance=self.image.get_width()//x
                k=1/2
                for i in range(1,x+1):
                    i=(i+1)//2
                    if mouse_pressed[0]:  # Left mouse button.
                        # Create a new bullet instance and add it to the groups.
                        Bullet((cor[0]+(i*k*distance),cor[1]), self.bullet_img,self.bullet_vel,self.bullet_damage, self.all_sprites, self.bullets)
                        self.laser_sound.play()
                        self.bullet_timer = self.bullet_time  # Reset the timer.
                        k*=-1
                        


    def update(self, dt):
        if self.health <= 0:
            self.kill()
            self.hero_death=True
        if not self.hero_death:
            if not self.amIGhost:
                hero_bullet=pg.sprite.spritecollide(self,self.enemy_bullets,True) 
                enemy_Hero=pg.sprite.spritecollide(self,self.enemies,True)
                if len(hero_bullet)==1:
                    self.health-=hero_bullet[0].get_damage()
                if len(enemy_Hero)==1:
                    self.health-=enemy_Hero[0].get_damage()  
            drop_Hero=pg.sprite.spritecollide(self,self.drops,True)
            if len(drop_Hero)==1:
                self.welcome_drop(drop_Hero[0].get_effect())
            self.move()
            self.animation()
            self.fire(dt,self.cor,self.firex)
            self.healthbar(self.screen)
            self.atack_skill(dt)
            self.defense_skill(dt)

    def welcome_drop(self,list):
        
        if list[0]=="power":
            self.firex+=list[1]
        else:
            self.max_health+=list[1]
            self.health=self.max_health

    def draw_hero(self,screen,font):

        hero_name = font.render(f"{self.__class__.__name__}", True, (255, 255, 255))
        hero_name_rect = hero_name.get_rect(center=(self.rect.center[0],self.rect.center[1]+128))
        self.rect.center=(screen.get_width() // 2, screen.get_height() // 2+64)
        screen.blit(self.image,self.rect)
        self.animation()
        screen.blit(hero_name,hero_name_rect)


    def get_width(self):
        return self.image.get_width()

    def animation(self):
        mouse_pressed = pg.mouse.get_pressed()
        image=self.animated[int(self.current_animated)]
        self.current_animated+=0.3
        if mouse_pressed[0]:
            self.current_image+=0.2
        if self.current_animated>=3:
            self.current_animated=0
        if self.current_image >= len(self.image_list):
            self.current_image = 0
        rect=image.get_rect(center=(self.rect.center[0],self.rect.center[1]+32))
        self.image=self.image_list[int(self.current_image)]
        if self.amIGhost:
            self.image.set_alpha(150)
        else:
            self.image.set_alpha(255)
        self.screen.blit(image,rect)


    def get_height(self):
        return self.image.get_height()

    def healthbar(self, window):
            pg.draw.rect(window, (255, 0, 0),(self.rect.x, self.rect.y + self.get_height() + 20, self.get_width(), 10))
            pg.draw.rect(window, (0, 255, 0), (self.rect.x, self.rect.y + self.get_height() + 20, self.get_width() * (self.health / self.max_health), 10))
    def defense_skill(self):
        if self.defenseSkill:
            self.health+=10
            if self.health>=self.max_health:
                self.health=self.max_health
            self.defenseSkill=False

    def atack_skill(self,dt):
        if self.atackSkill:

            center=(self.screen.get_width() - self.rect.center[0], self.rect.center[1])
            image=self.image.copy()
            rect = image.get_rect(center=center)
            image.set_alpha(80)
            self.screen.blit(self.image, rect)
            self.fire(dt,center,self.firex)
            self.cooldown_atack-=dt
            if self.cooldown_atack<=0:
                self.atackSkill=False
                self.cooldown_atack=5

    def item1_efect(self,increase):

        self.bullet_time-=increase
        
    
    def item2_efect(self,increase):

        self.bullet_damage+=increase

    def keyCheck(self,key,bool):
        if key=="e" and bool:
            pg.mixer.Sound("sound\\mixkit-robot-system-fail-2960.wav").play()
            self.atackSkill=True
        elif key=="q" and bool:
            self.defenseSkill=True



class Tank(Heros):


    def __init__(self, pos,window, all_sprites, bullets,sprite_groups,enemy_bullets,enemies,drops):
        super(Tank, self).__init__( pos,window, all_sprites, bullets,sprite_groups,enemy_bullets,enemies,drops)
        self.image_list =[pg.image.load("image\\hr1.png"),pg.image.load("image\\hr4.png"),pg.image.load("image\\hr1.png"), pg.image.load("image\\hr2.png"), pg.image.load("image\\hr3.png"), pg.image.load("image\\hr2.png"), pg.image.load("image\\hr1.png")]
        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.image.convert()
        self.bullet_time = 0.8
        self.health = 150
        self.max_health = 150
        self.screen = window
        self.bullet_damage = 15
        self.bullet_vel = (0, -300)
        self.defenseSkill=False
        self.atackSkill=False
        self.amIGhost=False

    def defense_skill(self):
        if self.defenseSkill:
            self.health+=10
            if self.health>=self.max_health:
                self.health=self.max_health
            self.defenseSkill=False

    def atack_skill(self,dt):
        if self.atackSkill:

            center=(self.screen.get_width() - self.rect.center[0], self.rect.center[1])
            rect = self.image.get_rect(center=center)
            self.screen.blit(self.image, rect)
            self.fire(dt,center)
            self.cooldown_atack-=dt
            if self.cooldown_atack<=0:
                self.atackSkill=False
                self.cooldown_atack=5


class Ghost(Heros):


    def __init__(self,pos,window, all_sprites, bullets,sprite_groups,enemy_bullets,enemies,drops):
        super(Ghost, self).__init__( pos,window, all_sprites, bullets,sprite_groups,enemy_bullets,enemies,drops)
        self.image_list = [pg.image.load("image\\hero1.png"), pg.image.load("image\\hero2.png"), pg.image.load("image\\hero3.png"),
                           pg.image.load("image\\hero4.png"), pg.image.load("image\\hero3.png"), pg.image.load("image\\hero2.png"),
                           pg.image.load("image\\hero1.png")]
        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.rect=self.image.get_rect(center=pos)
        self.bullet_time = 0.5
        self.health = 100
        self.max_health = 100
        self.screen = window
        self.bullet_damage = 25
        self.bullet_vel = (0, -450)
        self.cooldown_atack=4
        self.cooldown_defense=8
        self.defenseSkill=False
        self.atackSkill=False
        self.amIGhost=False

    def defense_skill(self,dt):
        if self.defenseSkill:
            self.cooldown_defense-=dt
            self.amIGhost=True
            if self.cooldown_defense<=0:
                self.defenseSkill=False
                self.amIGhost=False
                self.cooldown_defense=8

    def atack_skill(self,dt):
        if self.atackSkill:

            center=(self.screen.get_width() - self.rect.center[0], self.rect.center[1])
            image=self.image.copy()
            rect = image.get_rect(center=center)
            image.set_alpha(150)
            self.screen.blit(image, rect)
            self.fire(dt,center,self.firex)
            self.cooldown_atack-=dt
            if self.cooldown_atack<=0:
                self.atackSkill=False
                self.cooldown_atack=4






