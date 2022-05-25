import pygame as pg
from BULLET import *
class Heros(pg.sprite.Sprite):


    def __init__(self, pos,window, all_sprites, bullets,sprite_groups):
        super(Heros, self).__init__(sprite_groups)
        self.hero_death=False
        self.cor=pos
        self.image_list=[pg.image.load("hr3.png"),pg.image.load("hr2.png"),pg.image.load("hr1.png"),pg.image.load("hr4.png"),pg.image.load("hr1.png"),pg.image.load("hr2.png"),pg.image.load("hr3.png")]
        self.current_image=0
        self.image = self.image_list[self.current_image]
        self.rect = self.image.get_rect(center=self.cor)
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets
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
        self.animated=[pg.image.load("Untitled (1).png"),pg.image.load("Untitled (2).png"),pg.image.load("Untitled (3).png")]
        self.atackSkill=False
        self.defenseSkill=False
        self.laser_sound = pg.mixer.Sound('laser.wav')
        self.laser_sound.set_volume(0.3)

    def move(self):
        self.cor=pg.mouse.get_pos()
        self.rect.center = self.cor

    def fire(self,dt,cor):
        mouse_pressed = pg.mouse.get_pressed()
        self.bullet_timer -= dt  # Subtract the time since the last tick.
        if self.bullet_timer <= 0:
            self.bullet_timer = 0  # Bullet ready.
            if mouse_pressed[0]:  # Left mouse button.
                # Create a new bullet instance and add it to the groups.
                Bullet(cor, self.bullet_img,self.bullet_vel,self.bullet_damage, self.all_sprites, self.bullets)
                self.laser_sound.play()
                self.bullet_timer = self.bullet_time  # Reset the timer.

    def update(self, dt):
        if self.health <= 0:
            self.kill()
            self.hero_death=True
        if not self.hero_death:
            self.move()
            self.animation()
            self.fire(dt,self.cor)
            self.healthbar(self.screen)
            self.atack_skill(dt)
            self.defense_skill()



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
            rect = self.image.get_rect(center=center)
            self.screen.blit(self.image, rect)
            self.fire(dt,center)
            self.cooldown_atack-=dt
            if self.cooldown_atack<=0:
                self.atackSkill=False
                self.cooldown_atack=5
    def keyCheck(self,bool):
        if bool=="e":
            self.atackSkill=True
        elif bool=="q":
            self.defenseSkill=True



class Tank(Heros):


    def __init__(self, pos,window, all_sprites, bullets,sprite_groups):
        super(Tank, self).__init__( pos,window, all_sprites, bullets,sprite_groups)
        self.image_list = [pg.image.load("hr1.png"),pg.image.load("hr4.png"),pg.image.load("hr1.png"), pg.image.load("hr2.png"), pg.image.load("hr3.png"), pg.image.load("hr2.png"), pg.image.load("hr1.png")]
        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.bullet_time = 0.6
        self.health = 150
        self.max_health = 150
        self.screen = window
        self.bullet_damage = 15
        self.bullet_vel = (0, -300)


class Ghost(Heros):


    def __init__(self,pos,window, all_sprites, bullets,sprite_groups):
        super(Ghost, self).__init__( pos,window, all_sprites, bullets,sprite_groups)
        self.image_list = [pg.image.load("hero1.png"), pg.image.load("hero2.png"), pg.image.load("hero3.png"),
                           pg.image.load("hero4.png"), pg.image.load("hero3.png"), pg.image.load("hero2.png"),
                           pg.image.load("hero1.png")]
        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.rect=self.image.get_rect(center=pos)
        self.bullet_time = 0.2
        self.health = 100
        self.max_health = 100
        self.screen = window
        self.bullet_damage = 25
        self.bullet_vel = (0, -450)
        self.cooldown_atack=5






