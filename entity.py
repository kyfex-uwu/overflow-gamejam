import pygame


class Entity:
    def __init__(self, x, y, w, h):
        self.level = None
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def init(self, level):
        level.entities.append(self)
        self.level = level

    def render(self):
        pygame.draw.rect(self.level.surface, pygame.Color(255,0,0),
                         pygame.Rect(self.x,self.y,self.w,self.h))

    def tick(self):
        self.x+=1