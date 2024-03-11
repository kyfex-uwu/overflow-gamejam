import math
import os

import pygame

from screen.component.component import Component

wrap_amt = 0
class WrapImage(Component):
    def __init__(self, img_name, offs):
        super().__init__()
        self.offs = offs
        self.image = pygame.image.load(os.path.join('resources', img_name+'.png')).convert_alpha()
    def render(self, screen):
        global wrap_amt
        wrap_amt = (wrap_amt+0.015)%(math.pi*2)
        amt = round(math.sin(wrap_amt)*8+self.offs)
        screen.blit(self.image, (0, 3), (2 - amt, 0, 176, 99))
        screen.blit(self.image, (amt - 8-self.offs, 3), (171-self.offs, 0, 8, 99))
        screen.blit(self.image, (175 + amt, 3), (0, 0, 9-self.offs, 99))
