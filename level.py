import pygame
from pygame import Surface

from entity.entity import Vector

PIXEL_WIDTH=5
vfactor = 3

class Level:
    def __init__(self, w, h): # in tiles
        self.w=max(32,w)
        self.h=max(18,h)
        self.x=0
        self.y=0
        self.surface = Surface((self.w*8,self.h*8))
        self.screenSize=Vector(0,0)

        self.entities = []
        self.default_spawn = None
        self.player_entity = None

    def set_screen_size(self, dest:Surface):
        self.screenSize = Vector(dest.get_width() / PIXEL_WIDTH, dest.get_height() / PIXEL_WIDTH)

    def render(self, dest: Surface):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y = max(0, self.y - vfactor)
        if keys[pygame.K_DOWN]:
            self.y = min(self.h*8-dest.get_height()/PIXEL_WIDTH, self.y + vfactor)
        if keys[pygame.K_LEFT]:
            self.x = max(0, self.x - vfactor)
        if keys[pygame.K_RIGHT]:
            self.x = min(self.w*8-dest.get_width()/PIXEL_WIDTH, self.x + vfactor)

        self.surface.fill(pygame.Color(0,0,0))

        for entity in self.entities:
            entity.render()
        pygame.transform.scale(self.surface.subsurface(
                (self.x,self.y,dest.get_width()/PIXEL_WIDTH,dest.get_height()/PIXEL_WIDTH)),
            (dest.get_width(),dest.get_height()),
            dest)
    def tick(self):
        for entity in self.entities:
            entity.tick()
