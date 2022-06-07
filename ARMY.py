from numpy import mat
from scipy import rand
import math
from Sprites import *
from ENEMIES import *
import random
import pygame as pg
from DROPS import *

class Army(Sprite):


    def __init__(self, all_sprites,bullets,enemies,screen,hero_bullets,drop_sprite,wallet):
        super(Army, self).__init__(all_sprites)
        self.image=None
        self.all_sprites = all_sprites
        self.bullets_sprite = bullets
        self.enemies_sprite=enemies
        self.drop_sprite=drop_sprite
        self.hero_bullets=hero_bullets
        self.screen=screen
        self.wallet=wallet
        self.score=0
        self.coins=0
        self.xart=1
        self.yart=1
        self.x=0
        self.y=0
        self.firex=2
        self.functionX=1
        self.cooldown=0
        self.armyNumbers=0
        self.speed=1
        self.enemies=[]
        self.drop_numbers=random.randint(0,2)
        self.armyWidth=[int(self.screen.get_width()/8),int(self.screen.get_width()*15/16),int(self.screen.get_width()*2/16)]
        self.armyHeight=[int(self.screen.get_height()/8),int(self.screen.get_height()*5/8),int(self.screen.get_height()*1.2/8)]
        

    def update(self,dt):
        cor=self.functions(self.armyNumbers)
        for enemy in self.enemies:
            if not enemy.alive():
                self.get_score(enemy)
                if random.choice([0,0,0,0,0,1]):
                    self.creating_drop(enemy)
                self.enemies.remove(enemy)
            self.move_army(enemy,cor)
            self.Did_touch_enemy(enemy,dt)
        if len(self.enemies)==0:
            self.selectArmy()
            self.creating_army(self.speed)

    def creating_army(self,speed):
        self.x=0
        self.y=0
        self.drop_numbers=random.randint(0,3)
        self.speed = speed + 0.6
        self.enemies_list = Enemy.__subclasses__()
        self.enemies = []
        i=50
        for x in range(int(self.armyWidth[0]),int(self.armyWidth[1]),int(self.armyWidth[2])):
                for y in range(int(self.armyHeight[0]),int(self.armyHeight[1]),int(self.armyHeight[2])):
                   self.enemies.append(random.choice(self.enemies_list)((x+i,y),self.speed,self.all_sprites,self.bullets_sprite,self.enemies_sprite,self.screen,self.hero_bullets,self.wallet))
                   i*=-1
    
    def creating_drop(self,enemy):
        my_drops=Drops.__subclasses__()
        if self.drop_numbers>=1:
            if self.firex<6:
                random.choice(my_drops)((enemy.get_pos()),self.all_sprites,self.drop_sprite,self.hero_bullets,self.screen,self.firex)
            else:
                my_drops[random.randint(1,len(my_drops)-1)]((enemy.get_pos()),self.all_sprites,self.drop_sprite,self.hero_bullets,self.screen,self.firex)
            self.drop_numbers-=1

    def Did_touch_enemy(self,enemy,dt):
        self.cooldown-=dt
        if enemy.Did_touch() and self.cooldown<0:
            self.xart*= -1
            self.cooldown=1

    def move_army(self,enemy,tuple):

        enemy.move(tuple[0],tuple[1])

    
    def get_score(self,enemy):

            score,coins=self.score,self.coins
            self.score,self.coins= enemy.get_score_coin(score,coins)[0],enemy.get_score_coin(score,coins)[1]     


    def send_score(self,score):
        score+=self.score
        self.score=0
        return score

    def send_coins(self,coin):
        coin+=self.coins
        self.coins=0
        return coin
    
    def fireX(self,value):

        self.firex=value+1
    
    def functions(self,thefunction:int):
        if thefunction==1:
            self.x+=self.xart
            return (self.x,self.y)
        elif thefunction==2:
            self.x+=self.xart
            y=35*math.sin(self.x)
            x=self.x+3*self.xart
            return (10*x,y) 
        #self.functionX arttır
    def selectArmy(self):
        self.armyNumbers+=1
        if self.armyNumbers==2:
            self.xart=0.04
        else:
            self.xart+=0.003
        if self.armyNumbers>2:
            self.armyNumbers=2
            self.armyWidth[2]=int(self.armyWidth[2]*(0.9))
            self.armyHeight[2]=int(self.armyHeight[2]*(0.9))

            

