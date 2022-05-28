import pygame

#artış fonksiyon

class Wallet(pygame.sprite.Sprite):

 
    def __init__(self,all_sprite, wallet_sprite,screen,font) -> None:
        super(Wallet,self).__init__(wallet_sprite)
        self.image=pygame.image.load("coin.png")
        self.coins=0
        self.all_sprites=all_sprite
        self.add(self.all_sprites)
        self.screen=screen
        self.font = font
        self.rect=self.image.get_rect(bottomright=(self.screen.get_width(),self.image.get_height()))

    
    def Am_I_Rich(self,fee):
        if fee<=self.coins:
            self.coins-=fee
            return True

    def update(self,dt) -> None:
        self.coins_label=self.font.render(str(self.coins), True, (255, 255, 255))
        rect=self.coins_label.get_rect(bottomright=( self.screen.get_width()-self.image.get_width(),self.image.get_height()))
        self.screen.blit(self.coins_label,rect)

    def my_coins(self):
        return self.coins
    
    def update_wallet(self,coins):
        self.coins+=coins

        
        