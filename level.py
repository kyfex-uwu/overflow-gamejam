import math
import os

import pygame
from pygame import Surface

import globalvars
import keys
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

    def render(self, dest: Surface):
        self.surface.fill((0,0,0))

        for entity in self.entities:
            entity.render()

        dest.blit(self.surface, (round(-self.x), round(-self.y),self.screenSize.x,self.screenSize.y))

    def tick(self):
        if keys.SCR_RIGHT.down:
            self.xVel = min(self.xVel + 0.4, 2)
        if keys.SCR_LEFT.down:
            self.xVel = max(self.xVel - 0.4, -2)
        self.x+=self.xVel

        if self.player_entity is not None:
            self.y = self.y * 0.9 + (self.player_entity.y - self.screenSize.y / 5 * 3) * 0.1

        self.y = max(0, min(self.h * 8 - self.screenSize.y, self.y))
        self.x = max(0, min(self.w * 8 - self.screenSize.x, self.x))

        self.entities.sort(key=lambda e: e.z)
        for entity in self.entities:
            entity.tick()

        self.xVel = round(self.xVel * 0.8 * 1000) / 1000
        if abs(self.xVel) <= 0.002: self.xVel = 0
