from re import A
from ENEMIES import *
import random
import pygame as pg

class Army():


    def __init__(self, all_sprites,bullets,enemies,screen,hero_bullets):
        self.all_sprites = all_sprites

        self.bullets_sprite = bullets
        self.enemies_sprite=enemies
        self.screen=screen
        self.hero_bullets=hero_bullets
        self.score=0
        self.coins=0
        self.enemies=[]

    def update(self):
        for enemy in self.enemies:
               if self.get_score(enemy):    
                 self.enemies.remove(enemy)

    def creating_army(self,speed):

        self.speed = speed + 0.6
        self.enemies_list = Enemy.__subclasses__()
        self.enemies = []
        for x in range(200,1300,200):
                i=-50
                for y in range(150,451,100):
                   self.enemies.append(random.choice(self.enemies_list)((x+i,y),self.speed,self.all_sprites,self.bullets_sprite,self.enemies_sprite,self.screen,self.hero_bullets))
                   i+=50

    def move_army(self,left):

        for enemy in self.enemies:
            pass
    
    def get_score(self,enemy):

        if pg.sprite.Sprite.alive(enemy):
            score,coins= enemy.get_score_coin()[0],enemy.get_score_coin()[1]
            self.score +=score
            self.coins+=coins
            if score>0:
                return True

    def send_score(self):
        return self.score

    def send_coins(self):
        x,self.coins=self.coins,0
        return x


