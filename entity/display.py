import os

import pygame

import level_loader
from entity.entity import Entity


class DisplayEntity(Entity):
    def __init__(self, x, y, img_name):
        super().__init__(x, y, 0, 0)
        self.image = pygame.image.load(os.path.join('resources', 'display', img_name+'.png'))

    def render(self):
        self.level.surface.blit(self.image, (self.x, self.y))

def init():
    def loader(strings):
        return DisplayEntity(int(strings[0]), int(strings[1]), strings[2])
    level_loader.ENTITY_LOADERS['display'] = loader
