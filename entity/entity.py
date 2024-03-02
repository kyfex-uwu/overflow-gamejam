import pygame


class Entity:
    def __init__(self, x, y, w, h):
        self.level = None
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xVel = 0
        self.yVel = 0

    def init(self, level):
        level.entities.append(self)
        self.level = level

    def colliding(self, other):
        return (other.x - self.w <= self.x <= other.x + other.w and
                other.y - self.h <= self.y <= other.y + other.h)

    def render(self):
        pygame.draw.rect(self.level.surface, pygame.Color(0,0,150),
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
