from operator import truth
from warnings import warn

import pygame

from pygame.rect import Rect
from pygame.time import get_ticks
from pygame.mask import from_surface


class Sprite(object):

    def __init__(self, *groups):
        self.__g = {}  # The groups the sprite is in
        if groups:
            self.add(*groups)

    def add(self, *groups):

        has = self.__g.__contains__
        for group in groups:
            if hasattr(group, "_spritegroup"):
                if not has(group):
                    group.add_internal(self)
                    self.add_internal(group)
            else:
                self.add(*group)

    def remove(self, *groups):

        has = self.__g.__contains__
        for group in groups:
            if hasattr(group, "_spritegroup"):
                if has(group):
                    group.remove_internal(self)
                    self.remove_internal(group)
            else:
                self.remove(*group)

    def add_internal(self, group):
 
        self.__g[group] = 0

    def remove_internal(self, group):

        del self.__g[group]

    def update(self, *args, **kwargs):
        pass
    def kill(self):
        for group in self.__g:
            group.remove_internal(self)
        self.__g.clear()
    def alive(self):

        return truth(self.__g)

    def spritecollide(self, group):
   
        default_sprite_collide_func = self.rect.colliderect
        return [group_sprite for group_sprite in group  if default_sprite_collide_func(group_sprite.rect) ]
