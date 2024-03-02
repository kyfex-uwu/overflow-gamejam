import os
import pygame
from entity.solid import SolidEntity

class TileColl(SolidEntity):
    def render(self): pass

class Tiles(SolidEntity):
    def __init__(self, palette, tileStr: str):
        super().__init__(0, 0, 0, 0)
        self.palette = palette

        rows = tileStr.split("\n")
        self.w = len(sorted(rows, key=lambda row: len(row), reverse=True)[0])
        self.h = len(rows)

        self.tiles = []
        self.tileColls = []
        paletteImages = set()
        for y in range(self.h):
            self.tiles.append([])
            rowLength = len(rows[y])
            for x in range(self.w):
                if x >= rowLength or rows[y][x] == ".":
                    self.tiles[y].append(None)
                else:
                    self.tiles[y].append(palette[rows[y][x]])
                    self.tileColls.append(TileColl(x*8,y*8,8,8))
                    paletteImages.add(palette[rows[y][x]][2])
        self.images = {}
        for image in paletteImages:
            self.images[image] = pygame.image.load(os.path.join('resources', image + '.png')).convert_alpha()

    def init(self, level):
        super().init(level)
        for tileColl in self.tileColls:
            tileColl.init(level)

    def render(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.tiles[y][x] is None: continue
                self.level.surface.blit(self.images[self.tiles[y][x][2]], (x * 8, y * 8),
                                        (self.tiles[y][x][0]*8,self.tiles[y][x][1]*8, 8, 8))
