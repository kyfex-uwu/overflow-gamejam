import pygame
from pygame import Surface

PIXEL_WIDTH=5
vfactor = 3

class Level:
    def __init__(self, w, h): # in tiles
        self.w=w
        self.h=h
        self.x=0
        self.y=0
        self.surface = Surface((w*8,h*8))

        self.entities = []

    def render(self, dest: Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y = max(0, self.y - vfactor)
        if keys[pygame.K_DOWN]: # test_level.y - vfactor*dt <= test_level.h
            self.y = min(self.h, self.y + vfactor)
        if keys[pygame.K_LEFT]:
            self.x = max(0, self.x - vfactor)
        if keys[pygame.K_RIGHT]:
            self.x = min(self.w, self.x + vfactor)

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
