from numpy import mat
from scipy import rand
import math
from Sprites import *
from ENEMIES import *
import random
import pygame as pg
from DROPS import *

class Army(Sprite):


    def __init__(self, all_sprites,screen,game):
        super(Army, self).__init__(all_sprites)
        self.EUE=game
        self.image=None
        self.screen=screen
        self.score=0
        self.coins=0
        self.xart=1
        self.yart=1
        self.x=0
        self.y=0
        self.cooldown=0
        self.armyNumbers=0
        self.speed=1
        self.enemies=[]
        self.mydrop=None
        self.drop_numbers=random.randint(0,2)
        self.armyWidth=[int(self.screen.get_width()/8),int(self.screen.get_width()*15/16),int(self.screen.get_width()*2/16)]
        self.armyHeight=[int(self.screen.get_height()/8),int(self.screen.get_height()*5/8),int(self.screen.get_height()*1.2/8)]
        

    def update(self,dt):
        cor=self.functions(self.armyNumbers)
        for enemy in self.enemies:
            if not enemy.alive():
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
        objects=self.EUE.HereIsX(all_sprites=1,enemies_sprites=1)
        for x in range(int(self.armyWidth[0]),int(self.armyWidth[1]),int(self.armyWidth[2])):
                for y in range(int(self.armyHeight[0]),int(self.armyHeight[1]),int(self.armyHeight[2])):
                   self.enemies.append(random.choice(self.enemies_list)((x+i,y),self.speed,self.screen,objects[0],objects[1],self))
                   i*=-1
    
    def creating_drop(self):
        my_drops=Drops.__subclasses__()
        if self.drop_numbers>=1:
            objects=self.EUE.HereIsX(all_sprites=1,hero_sprite=1,drops_sprites=1,hero_bullets=1)
            self.mydrop=random.choice(my_drops)(self.speed+1,self.screen,objects[0],objects[1],objects[2],objects[3])
            self.drop_numbers-=1
            return True
        else:
            return False

    def Did_touch_enemy(self,enemy,dt):
        self.cooldown-=dt
        if enemy.Did_touch() and self.cooldown<0:
            self.xart*= -1
            self.cooldown=1

    def move_army(self,enemy,tuple):

        enemy.move(tuple[0],tuple[1])
    
    def functions(self,thefunction:int):
        if thefunction==1:
            self.x+=self.xart
            return (self.x,self.y)
        elif thefunction==2:
            self.x+=self.xart
            y=35*math.sin(self.x)
            x=self.x+3*self.xart
            return (10*x,y) 

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
    
    def HereIsX(self,drop=0,game=0):
        if drop:   
            if random.choice([0,0,0,0,0,1]):
                        if self.creating_drop():
                            return self.mydrop
                        else:
                            return 0 
            else:
                return 0   
        elif game:
            return self.EUE
        else:
            return 0

    
       
            

