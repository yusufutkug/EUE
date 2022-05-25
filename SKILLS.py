import pygame

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
                self.cooldown_time=10
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

class defense_skill(Skills):


    def __init__(self,all_sprites,skills_sprite):
        super(defense_skill, self).__init__(all_sprites,skills_sprite)
        self.image_list = [pygame.image.load("shield.png")]
                          # pygame.image.load("shield2.png"),pygame.image.load("shield2.png"),pygame.image.load("shield1.png")]
                           # pygame.image.load("shield4.png"), pygame.image.load("shield5.png"),
                           # pygame.image.load("shield6.png"), pygame.image.load("shield5.png"),
                           # pygame.image.load("shield4.png"), pygame.image.load("shield3.png"), pygame.image.load("shield2.png"), pygame.image.load("shield1.png"), pygame.image.load("shield.png")]
        self.image_cooldown =  [pygame.image.load("pshield.png")]
                           # pygame.image.load("pshield2.png"), pygame.image.load("pshield3.png"),
                           # pygame.image.load("pshield4.png"), pygame.image.load("pshield5.png"),
                           # pygame.image.load("pshield6.png"), pygame.image.load("pshield5.png"),
                           # pygame.image.load("pshield4.png"), pygame.image.load("pshield3.png"), pygame.image.load("pshield2.png"), pygame.image.load("pshield.png")]


        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.cor = (100, 780)
        self.rect = self.image.get_rect(bottomleft=self.cor)
        self.cooldown = False
        self.cooldown_time = 10
        self.wait_time=0.09



class atack_skill(Skills):


    def __init__(self,all_sprites,skills_sprite):
        super(atack_skill, self).__init__(all_sprites,skills_sprite)
        self.image_list = [pygame.image.load("kılıç1.png"), pygame.image.load("kılıç2.png"),
                           pygame.image.load("kılıç3.png"), pygame.image.load("kılıç4.png"),
                           pygame.image.load("kılıç5.png"), pygame.image.load("kılıç5.png"),
                           pygame.image.load("kılıç4.png"), pygame.image.load("kılıç3.png"),
                           pygame.image.load("kılıç2.png")]
        self.image_cooldown = [pygame.image.load("ışın.png"), pygame.image.load("ışın2.png"),
                               pygame.image.load("ışın3.png"),
                               pygame.image.load("ışın4.png"), pygame.image.load("ışın5.png"),
                               pygame.image.load("ışın6.png"),
                               pygame.image.load("ışın7.png"), pygame.image.load("ışın8.png"),
                               pygame.image.load("ışın8.png"),
                               pygame.image.load("ışın7.png"), pygame.image.load("ışın6.png"),
                               pygame.image.load("ışın5.png"),
                               pygame.image.load("ışın4.png"), pygame.image.load("ışın3.png"),
                               pygame.image.load("ışın2.png"),
                               pygame.image.load("ışın.png")]

        self.current_image = 0
        self.image = self.image_list[self.current_image]
        self.cor=(1400, 780)
        self.rect = self.image.get_rect(bottomleft=self.cor)
        self.cooldown = False
        self.cooldown_time = 10
        self.wait_time=0.2