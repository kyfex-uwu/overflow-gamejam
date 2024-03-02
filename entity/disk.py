import math
import os

import pygame

from entity.entity import Entity

class DiskEntity(Entity):
    IMAGE = None
    def __init__(self, x, y):
        super().__init__(x, y, 16,16)
        self.float_offs=0

        if DiskEntity.IMAGE is None:
            DiskEntity.IMAGE = pygame.image.load(os.path.join('resources', 'entity', 'disk.png')).convert_alpha()

    def render(self):
        self.float_offs=(self.float_offs+0.03)%(math.pi*2)
        self.level.surface.blit(DiskEntity.IMAGE, (self.x-4,self.y-4.5+math.sin(self.float_offs)*1.3))
