import os

import pygame

from entity.entity import Entity
from entity.solid import SolidEntity
from level_loader import ENTITY_LOADERS


class Tiles(Entity):
    def __init__(self, tiles, images):
        super().__init__(0, 0, 0, 0)
        self.w = len(tiles[0])
        self.h = len(tiles)

        self.tiles = tiles
        self.tileColls = []
        for y in range(self.h):
            self.tiles.append([])
            for x in range(self.w):
                if self.tiles[y][x] is not None:
                    self.tileColls.append(SolidEntity(x * 8, y * 8, 8, 8))

        self.images = {}
        for image in images:
            self.images[image] = pygame.image.load(os.path.join('resources', 'tiles', image + '.png')).convert_alpha()

    def init(self, level):
        super().init(level)
        for tileColl in self.tileColls:
            tileColl.init(level)

    def render(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.tiles[y][x] is None: continue
                self.level.surface.blit(self.images[self.tiles[y][x][2]], (x * 8, y * 8),
                                        (self.tiles[y][x][0] * 8, self.tiles[y][x][1] * 8, 8, 8))
def init():
    ENTITY_LOADERS['tiles'] = lambda args: Tiles(*args)
