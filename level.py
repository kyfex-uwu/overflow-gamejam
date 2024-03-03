import pygame
from pygame import Surface

from entity.entity import Vector
from entity.spawn import SpawnPointEntity

PIXEL_WIDTH=8

class Level:
    def __init__(self, w, h): # in tiles
        self.w=max(22,w)
        self.h=max(18,h)
        self.x=0
        self.y=0
        self.xVel=0
        self.surface = Surface((self.w*8,self.h*8), flags=pygame.SRCALPHA)
        self.screenSize=Vector(11*16,11*9)

        self.entities = []
        self.default_spawn = None
        self.player_entity = None

    def render(self, dest: Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.xVel=min(self.xVel+0.4,2)
        if keys[pygame.K_LEFT]:
            self.xVel=max(self.xVel-0.4,-2)

        self.x = max(0, min(self.w*8-self.screenSize.x, self.x + self.xVel))
        self.xVel*=0.8

        if self.player_entity is not None:
            self.y = max(0, min(self.h*8-self.screenSize.y,
                                self.y*0.9 + (self.player_entity.y-self.screenSize.y/5*3) * 0.1))

        self.surface.fill(pygame.Color(30,30,60))

        for entity in self.entities:
            entity.render()
        dest.blit(self.surface, (round(-self.x),round(-self.y),self.screenSize.x,self.screenSize.y))
    def tick(self):
        self.entities.sort(key=lambda e: e.z)
        for entity in self.entities:
            entity.tick()
