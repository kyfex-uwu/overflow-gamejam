import pygame
from pygame import Surface

PIXEL_WIDTH=5

class Level:
    def __init__(self, w, h): # in tiles
        self.w=w
        self.h=h
        self.x=0
        self.y=0
        self.surface = Surface((w*8,h*8))

        self.entities = []

    def render(self, dest: Surface):
        self.surface.fill(pygame.Color(0,0,0))

        for entity in self.entities:
            entity.render()

        pygame.transform.scale(self.surface.subsurface(
                pygame.Rect(self.x,self.y,dest.get_width()/PIXEL_WIDTH,dest.get_height()/PIXEL_WIDTH)),
            (dest.get_width(),dest.get_height()),
            dest)
    def tick(self):
        for entity in self.entities:
            entity.tick()
