import math
import os

import pygame
from pygame import Surface

import globalvars
from entity.entity import Vector

PIXEL_WIDTH=8

class Level:
    def __init__(self, w, h): # in tiles
        self.w=max(22,w)
        self.h=max(13,h)
        self.x=0
        self.y=0
        self.xVel=0
        self.surface = Surface((self.w*8,self.h*8), flags=pygame.SRCALPHA)
        self.screenSize=Vector(11*16,11*9)

        self.entities = []
        self.default_spawn = None
        self.player_entity = None

        self.finished = False
        self.started = False

    def render(self, dest: Surface):
        if not self.started:
            self.surface.fill((0,0,0))
            self.started = True
        else:
            self.surface.fill((0,0,0,70))
        self.x = max(0, min(self.w * 8 - self.screenSize.x, self.x + self.xVel))
        self.y = max(0, min(self.h * 8 - self.screenSize.y, self.y))

        for entity in self.entities:
            entity.render()

        dest.blit(self.surface, (-self.x, -self.y,self.screenSize.x,self.screenSize.y))

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.xVel = min(self.xVel + 0.4, 2)
        if keys[pygame.K_LEFT]:
            self.xVel = max(self.xVel - 0.4, -2)

        self.xVel *= 0.8

        if self.player_entity is not None:
            self.y = self.y * 0.9 + (self.player_entity.y - self.screenSize.y / 5 * 3) * 0.1

        self.entities.sort(key=lambda e: e.z)
        for entity in self.entities:
            entity.tick()
