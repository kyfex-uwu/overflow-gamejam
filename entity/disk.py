import math
import os

import pygame

import level_loader
from entity.entity import Entity
import audio

class DiskEntity(Entity):
    IMAGE = None
    def __init__(self, x, y):
        super().__init__(x, y, 16,16)
        self.z=-10
        self.float_offs=0
        self.collected=False

        if DiskEntity.IMAGE is None:
            DiskEntity.IMAGE = pygame.image.load(os.path.join('resources', 'entity', 'disk.png'))

    def render(self):
        self.float_offs=(self.float_offs+0.03)%(math.pi*2)
        self.level.surface.blit(DiskEntity.IMAGE, (self.x-4,self.y-4.5+math.sin(self.float_offs)*1.3))

    def tick(self):
        super().tick()
        if self.collected is False and self.level.player_entity.colliding(self):
            self.collected=0
            audio.collect()
            WinEffect(self.x+8,self.y+4).init(self.level)
        if self.collected is not False:
            self.collected = min(1,self.collected+0.005)

            self.level.player_entity.x = (
                (self.x+8-self.level.player_entity.w/2)*self.collected+
                self.level.player_entity.x*(1-self.collected))
            self.level.player_entity.y = (
                (self.y+4-self.level.player_entity.h/2)*self.collected+
                self.level.player_entity.y*(1-self.collected))
            self.level.player_entity.yVel*=(1-self.collected)
            self.level.player_entity.xVel*=(1-self.collected)

class WinEffect(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0)
        self.surface=None
        self.timer=0
    def init(self, level):
        super().init(level)
        self.surface = pygame.Surface(self.level.surface.get_size())
    def render(self):
        self.timer=min(255,self.timer*0.98+255*0.02)
        self.surface.fill((self.timer, self.timer, self.timer))
        self.level.surface.blit(self.surface, (self.level.x,self.level.y), special_flags=pygame.BLEND_ADD)

def init():
    def loader(strings):
        return DiskEntity(int(strings[0]), int(strings[1]))
    level_loader.ENTITY_LOADERS['disk'] = loader
