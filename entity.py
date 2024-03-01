import pygame
import numpy as np

class Entity:
    def __init__(self, x, y, w, h, level=None):
        self.level = None
        if level is not None:
            self.init(level)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.huh=False

    def init(self, level):
        level.entities.append(self)
        self.level = level

    def render(self):
        pygame.draw.rect(self.level.surface, pygame.Color(255,0,0),
                         pygame.Rect(self.x,self.y,self.w,self.h))

    def tick(self):
        if self.x >= 200 or self.huh:
            self.x-=1
            self.huh=True
        elif not self.huh:
            self.x+=1
        if self.x <= 0:
            self.huh=False