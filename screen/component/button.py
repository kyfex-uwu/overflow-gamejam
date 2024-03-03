import pygame.mouse
import os

import globalvars
from screen.component.component import SizedComponent


class Button(SizedComponent):
    IMAGE = None
    def __init__(self, x, y, w, h, on_click, level="level1"):
        super().__init__(x, y, w, h)
        self.on_click=on_click
        self.level=level

        # if Button.IMAGE is None:
        #     Button.IMAGE = pygame.image.load(os.path.join('resources', 'button.png')).convert_alpha()

    def render(self, screen):
        super().render(screen)
        pos = pygame.mouse.get_pos()
        if (self.x<=pos[0]/globalvars.PIXEL_WIDTH<=self.x+self.w and
                self.y<=pos[1]/globalvars.PIXEL_WIDTH<=self.y+self.h and
                globalvars.MOUSE["left"] is False and globalvars.MOUSE["p_left"] is True):
            self.on_click(self.level)

        
