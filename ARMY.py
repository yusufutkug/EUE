from re import A
from ENEMIES import *
import random
import pygame as pg

class Army:


    def __init__(self, all_sprites,bullets,enemies,screen):

        self.all_sprites = all_sprites
        self.bullets_sprite = bullets
        self.enemies_sprite=enemies
        self.screen=screen

    def creating_army(self,speed):

        self.speed = speed + 0.6
        self.enemies_list = Enemy.__subclasses__()
        self.enemies = []
        for x in range(100,1436,200):
                i=-50
                for y in range(200,550,100):
                   self.enemies.append(random.choice(self.enemies_list)((x+i,y),self.speed,self.all_sprites,self.bullets_sprite,self.enemies_sprite,self.screen))
                   i+=50
    def move_army(self,left):
        for enemy in self.enemies:
            pass

