import os

import pygame

from entity.entity import Entity

DISK_IMAGE = pygame.image.load(os.path.join('resources', 'entity', 'disk.png')).convert_alpha()
class DiscEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 16,16)

    def render(self):
        pass