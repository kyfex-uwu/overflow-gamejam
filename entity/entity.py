import pygame


class Entity:
    def __init__(self, x, y, w, h, color=(255,0,0)):
        self.level = None
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rcolor = color[0]
        self.gcolor = color[1]
        self.bcolor = color[2]
        self.xVel = 0
        self.yVel = 0

    def init(self, level):
        level.entities.append(self)
        self.level = level

    def colliding(self, other):
        return (other.x - self.w <= self.x <= other.x + other.w and
                other.y - self.h <= self.y <= other.y + other.h)

    def render(self):
        if(self.rcolor>255 or self.rcolor < 0):
            self.rcolor=0
        if(self.gcolor>255  or self.gcolor < 0):
            self.gcolor=0
        if(self.bcolor>255  or self.bcolor < 0):
            self.bcolor=0
        pygame.draw.rect(self.level.surface, pygame.Color(self.rcolor, self.gcolor, self.bcolor),
                         pygame.Rect(round(self.x), round(self.y), self.w, self.h))

    def tick(self):
        pass

class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __repr__(self): return f"Point({self.x}, {self.y})"
class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __repr__(self): return f"Point({self.x}, {self.y}, {self.w}, {self.h})"
