import pygame

#artış fonksiyon

class Wallet(Sprite):

 
    def __init__(self,all_sprite,screen,font):

        super(Wallet,self).__init__(all_sprite)
        self.image=pygame.image.load("image\\coin.png")
        self.coins=0
        self.screen=screen
        self.font = font
        self.rect=self.image.get_rect(bottomright=(self.screen.get_width(),self.image.get_height()))
    
    def Am_I_Rich(self,fee):

        if fee<=self.coins:

            return True

    def update(self,dt) -> None:

        self.coins_label=self.font.render(str(self.coins), True, (255, 255, 255))
        rect=self.coins_label.get_rect(bottomright=( self.screen.get_width()-self.image.get_width(),self.image.get_height()))
        self.screen.blit(self.coins_label,rect)
    
    def update_wallet(self,coins,effect=1):

        self.coins+=coins*effect

        
        