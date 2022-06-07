from Sprites import *

class Group(object):
    _spritegroup=True
    def __init__(self,*sprites):
        self.spritedict = {}
        self.lostsprites = []
        self.add(*sprites)

    def sprites(self):

        return list(self.spritedict)

    def add_internal(self,sprite):

        self.spritedict[sprite] = None

    def remove_internal(self, sprite):

        lost_rect = self.spritedict[sprite]
        if lost_rect:
            self.lostsprites.append(lost_rect)
        del self.spritedict[sprite]

    def has_internal(self, sprite):

        return sprite in self.spritedict


   

    def __contains__(self, sprite):
        return self.has(sprite)

    def add(self, *sprites):

        for sprite in sprites:
   
            if isinstance(sprite, Sprite):
                if not self.has_internal(sprite):
                    self.add_internal(sprite)
                    sprite.add_internal(self)
            else:
                try:
       
                    self.add(*sprite)
                except (TypeError, AttributeError):
      
                    if hasattr(sprite, "_spritegroup"):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                self.add_internal(spr)
                                spr.add_internal(self)
                    elif not self.has_internal(sprite):
                        self.add_internal(sprite)
                        sprite.add_internal(self)

    def remove(self, *sprites):

        for sprite in sprites:
            if isinstance(sprite, Sprite):
                if self.has_internal(sprite):
                    self.remove_internal(sprite)
                    sprite.remove_internal(self)
            else:
                try:
                    self.remove(*sprite)
                except (TypeError, AttributeError):
                    if hasattr(sprite, "_spritegroup"):
                        for spr in sprite.sprites():
                            if self.has_internal(spr):
                                self.remove_internal(spr)
                                spr.remove_internal(self)
                    elif self.has_internal(sprite):
                        self.remove_internal(sprite)
                        sprite.remove_internal(self)

    def has(self, *sprites):

        if not sprites:
            return False  

        for sprite in sprites:
            if isinstance(sprite, Sprite):
          
                if not self.has_internal(sprite):
                    return False
            else:
                try:
                    if not self.has(*sprite):
                        return False
                except (TypeError, AttributeError):
                    if hasattr(sprite, "_spritegroup"):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                return False
                    else:
                        if not self.has_internal(sprite):
                            return False

        return True

    def update(self, *args, **kwargs):
    
        for sprite in self.sprites():
            sprite.update(*args, **kwargs)

    def draw(self, surface):

        sprites = self.sprites()
        if hasattr(surface, "blits"):
            self.spritedict.update(zip(sprites, surface.blits((spr.image, spr.rect) for spr in sprites if not spr.image==None)))
        else:
            for spr in sprites:
                self.spritedict[spr] = surface.blit(spr.image, spr.rect)
        self.lostsprites = []
        

        

    def clear(self, surface, bgd):

        if callable(bgd):
            for lost_clear_rect in self.lostsprites:
                bgd(surface, lost_clear_rect)
            for clear_rect in self.spritedict.values():
                if clear_rect:
                    bgd(surface, clear_rect)
        else:
            surface_blit = surface.blit
            for lost_clear_rect in self.lostsprites:
                surface_blit(bgd, lost_clear_rect, lost_clear_rect)
            for clear_rect in self.spritedict.values():
                if clear_rect:
                    surface_blit(bgd, clear_rect, clear_rect)



    
