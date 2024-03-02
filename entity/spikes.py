import pygame
import os

from entity.entity import Entity

class SpikeEntity(Entity):
    IMAGE = None
    def __init__(self, x, y, direction="up"):
        super().__init__(x, y, 8, 8)
        self.parse=(8,8,8,8)
        if direction=="up":
            self.parse=(0,0,8,8)
        elif direction=="right":
            self.parse=(8,0,8,8)
        elif direction=="left":
            self.parse=(0,8,8,8)

        if SpikeEntity.IMAGE is None:
            SpikeEntity.IMAGE = pygame.image.load(os.path.join('resources', 'spikes.png')).convert_alpha()

    def tick(self):
        if(self.level.player_entity.colliding(self)):
            self.level.player_entity.kill()

    def render(self, image="spikes"):
        self.level.surface.blit(SpikeEntity.IMAGE, (self.x, self.y), self.parse)