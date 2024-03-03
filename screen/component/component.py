import pygame.draw


class Component:
    def __init__(self):
        pass
    def render(self, screen):
        pass

class PositionedComponent(Component):
    def __init__(self, x, y):
        super().__init__()
        self.x=x
        self.y=y

class SizedComponent(PositionedComponent):
    def __init__(self, x, y, w, h):
        super().__init__(x,y)
        self.w=w
        self.h=h
    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x,self.y,self.w,self.h))
