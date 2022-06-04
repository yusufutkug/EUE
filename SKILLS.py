import pygame
from sympy import re

class Skills(pygame.sprite.Sprite):
 

    def __init__(self,all_sprites,skills_sprite):
        super(Skills, self).__init__(skills_sprite)
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.image_list=[]
        self.image_cooldown= []
        self.current_image=0
        self.image=None
        self.rect=None
        self.cooldown=False
        self.cooldown_time =10
        self.cooldown_timer = 40
        self.wait_time=0.2
        

    def update(self,dt):
        if self.cooldown:
            self.current_image+=self.wait_time
            if self.current_image >= len(self.image_cooldown):
                self.current_image = 0
            self.image =self.image_cooldown[int(self.current_image)]
            self.rect = self.image.get_rect(bottomleft=self.cor)
            self.cooldown_time-=dt
            if self.cooldown_time<=0:
                self.cooldown=False
                self.cooldown_time=self.cooldown_timer
        else:
            self.current_image+=self.wait_time
            if self.current_image >= len(self.image_list):
                self.current_image = 0
            self.image=self.image_list[int(self.current_image)]
            self.rect = self.image.get_rect(bottomleft=self.cor)


    def key_check(self,bool):
        self.cooldown=bool

    def trigger(self):
        if self.cooldown==True:
             return True
        else:
            return False
    def get_cooldown(self):

        if self.cooldown:
            return False
        else: 
           return True

class defense_skill(Skills):


    def __init__(self,all_sprites,skills_sprite):
        super(defense_skill, self).__init__(all_sprites,skills_sprite)
        self.image_list = [pygame.image.load("image\\shield.png")]
                          # pygame.image.load("shield2.png"),pygame.image.load("shield2.png"),pygame.image.load("shield1.png")]
                           # pygame.image.load("shield4.png"), pygame.image.load("shield5.png"),
                           # pygame.image.load("shield6.png"), pygame.image.load("shield5.png"),
                           # pygame.image.load("shield4.png"), pygame.image.load("shield3.png"), pygame.image.load("shield2.png"), pygame.image.load("shield1.png"), pygame.image.load("shield.png")]
        self.image_cooldown =  [pygame.image.load("image\\pshield.png")]
                           # pygame.image.load("pshield2.png"), pygame.image.load("pshield3.png"),
                           # pygame.image.load("pshield4.png"), pygame.image.load("pshield5.png"),
                           # pygame.image.load("pshield6.png"), pygame.image.load("pshield5.png"),
                           # pygame.image.load("pshield4.png"), pygame.image.load("pshield3.png"), pygame.image.load("pshield2.png"), pygame.image.load("pshield.png")]


        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.cor = (30,pygame.display.Info().current_h-30)
        self.rect = self.image.get_rect(bottomleft=self.cor)
        self.cooldown = False
        self.cooldown_time = 40
        self.cooldown_timer = 40
        self.wait_time=0.09



class atack_skill(Skills):


    def __init__(self,all_sprites,skills_sprite):
        super(atack_skill, self).__init__(all_sprites,skills_sprite)
        self.image_list = [pygame.image.load("image\\kılıç1.png"), pygame.image.load("image\\kılıç2.png"),
                           pygame.image.load("image\\kılıç3.png"), pygame.image.load("image\\kılıç4.png"),
                           pygame.image.load("image\\kılıç5.png"), pygame.image.load("image\\kılıç5.png"),
                           pygame.image.load("image\\kılıç4.png"), pygame.image.load("image\\kılıç3.png"),
                           pygame.image.load("image\\kılıç2.png")]
        self.image_cooldown = [pygame.image.load("image\\ışın.png"), pygame.image.load("image\\ışın2.png"),
                               pygame.image.load("image\\ışın3.png"),
                               pygame.image.load("image\\ışın4.png"), pygame.image.load("image\\ışın5.png"),
                               pygame.image.load("image\\ışın6.png"),
                               pygame.image.load("image\\ışın7.png"), pygame.image.load("image\\ışın8.png"),
                               pygame.image.load("image\\ışın8.png"),
                               pygame.image.load("image\\ışın7.png"), pygame.image.load("image\\ışın6.png"),
                               pygame.image.load("image\\ışın5.png"),
                               pygame.image.load("image\\ışın4.png"), pygame.image.load("image\\ışın3.png"),
                               pygame.image.load("image\\ışın2.png"),
                               pygame.image.load("image\\ışın.png")]

        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.cor=(pygame.display.Info().current_w-self.image.get_width()-30,pygame.display.Info().current_h-30)
        self.rect = self.image.get_rect(bottomright=self.cor)
        self.cooldown = False
        self.cooldown_time = 40
        self.cooldown_timer = 40
        self.wait_time=0.2
   
