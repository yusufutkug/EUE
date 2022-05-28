from numpy import mat
from scipy import rand
import math
from ENEMIES import *
import random
import pygame as pg
from DROPS import *

class Army():


    def __init__(self, all_sprites,bullets,enemies,screen,hero_bullets,drop_sprite):
        self.all_sprites = all_sprites
        self.bullets_sprite = bullets
        self.enemies_sprite=enemies
        self.drop_sprite=drop_sprite
        self.hero_bullets=hero_bullets
        self.screen=screen
        self.score=0
        self.coins=0
        self.art=0.04
        self.x=0
        self.enemies=[]
        self.drop_numbers=random.randint(0,3)

    def update(self,):
        self.x+=self.art
        y=35*math.sin(self.x)
        x=self.x+3*self.art
        for enemy in self.enemies:
            if self.get_score(enemy):
                if random.choice([0,0,0,0,0,1]):
                    self.creating_drop(enemy)
                self.enemies.remove(enemy)
            self.move_army(enemy,x,y)
            self.Did_touch_enemy(enemy)

    def creating_army(self,speed):
        self.x=0
        self.drop_numbers=random.randint(0,3)
        self.speed = speed + 0.6
        self.enemies_list = Enemy.__subclasses__()
        self.enemies = []
        for x in range(200,1300,200):
                i=-50
                for y in range(150,451,100):
                   self.enemies.append(random.choice(self.enemies_list)((x+i,y),self.speed,self.all_sprites,self.bullets_sprite,self.enemies_sprite,self.screen,self.hero_bullets))
                   i+=50
    
    def creating_drop(self,enemy):
        my_drops=Drops.__subclasses__()
        if self.drop_numbers>=1:
            random.choice(my_drops)((enemy.get_pos()),self.all_sprites,self.drop_sprite,self.hero_bullets,self.screen)
            self.drop_numbers-=1

    def Did_touch_enemy(self,enemy):
        if enemy.Did_touch():
            self.art*= -1

    def move_army(self,enemy,x,y):

        enemy.move(x,y)

    
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


