import pygame
from pygame import Surface

from entity.entity import Vector

PIXEL_WIDTH=8
vfactor = 3

class Level:
    def __init__(self, w, h): # in tiles
        self.w=max(32,w)
        self.h=max(18,h)
        self.x=0
        self.y=0
        self.surface = Surface((self.w*8,self.h*8), flags=pygame.SRCALPHA)
        self.screenSize=Vector(11*16,11*9)

        self.entities = []
        self.default_spawn = None
        self.player_entity = None

    def render(self, dest: Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = max(0, self.x - vfactor)
        if keys[pygame.K_RIGHT]:
            self.x = min(self.w*8-dest.get_width(), self.x + vfactor)

        if self.player_entity is not None:
            self.y = max(0, min(self.h*8-dest.get_height(),
                                self.y*0.9 + (self.player_entity.y-dest.get_height()/5*3) * 0.1))

        self.surface.fill(pygame.Color(30,30,60))

        for entity in self.entities:
            entity.render()
        dest.blit(self.surface, (round(-self.x),round(-self.y),dest.get_width(),dest.get_height()))
    def tick(self):
        self.entities.sort(key=lambda e: e.z)
        for entity in self.entities:
            entity.tick()
