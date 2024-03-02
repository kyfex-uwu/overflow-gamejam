import pygame
import os

from entity.solid import SolidEntity

class SpikeEntity(SolidEntity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def tick(self):
        if(self.level.player_entity.colliding()):
            self.level.player_entity.kill()

    def render(self, image):
        self.image = image
        pygame.image.load(os.path.join('resources', image + '.png')).convert_alpha()
        self.level.surface.blit(self.image, (self.x, self.y),
                                        (self.tiles[y][x][0]*8,self.tiles[y][x][1]*8, 8, 8))