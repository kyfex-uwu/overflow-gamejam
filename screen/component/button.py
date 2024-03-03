import pygame.mouse
import os

import globalvars
from screen.component.component import SizedComponent


class Button(SizedComponent):
    IMAGE = None
    def __init__(self, x, y, w, h, on_click, screen, level=None):
        super().__init__(x, y, w, h)
        self.on_click=on_click
        self.level=level
        self.screen = screen

        if Button.IMAGE is None:
            Button.IMAGE = pygame.image.load(os.path.join('resources', 'buttons.png')).convert_alpha()

        if isinstance(level, int):
            self.parse = ((level-1)*9, 0, 9, 9)
            self.send = "level" + str(level)
        else:
            self.parse = (144,0,9,9)
            self.send = None
            

    def render(self, screen):
        super().render(screen)
        pos = pygame.mouse.get_pos()
        if (self.x<=pos[0]/globalvars.PIXEL_WIDTH<=self.x+self.w and
                self.y<=pos[1]/globalvars.PIXEL_WIDTH<=self.y+self.h and
                globalvars.MOUSE["left"] is False and globalvars.MOUSE["p_left"] is True):
            if self.send is None:
                self.on_click()
            else:
                self.on_click(self.send)
        
        self.screen.screen.blit(Button.IMAGE, (self.x, self.y), self.parse)

        
