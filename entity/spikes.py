import pygame
import os

import level_loader
from entity.entity import Entity
class SpikeEntity(Entity):
    IMAGE = None
    def __init__(self, x, y, direction="up"):
        super().__init__(x, y, 4, 4)
        self.parse=(8,8,8,8)
        if direction=="up":
            self.parse=(0,0,8,8)
        elif direction=="right":
            self.parse=(8,0,8,8)
        elif direction=="left":
            self.parse=(0,8,8,8)

        if SpikeEntity.IMAGE is None:
            SpikeEntity.IMAGE = pygame.image.load(os.path.join('resources', 'entity', 'spikes.png')).convert_alpha()

    def tick(self):
        if(self.level.player_entity.colliding(self)):
            self.level.player_entity.kill()

    def render(self):
        self.level.surface.blit(SpikeEntity.IMAGE, (self.x-2, self.y-2), self.parse)

def init():
    level_loader.ENTITY_LOADERS['spike'] = lambda args: SpikeEntity(int(args[0]), int(args[1]), args[2])