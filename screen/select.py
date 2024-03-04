import math

import pygame
from pygame import Surface

import audio
import globalvars
import level_loader
from screen.component.button import Button
from screen.component.wrap_img import WrapImage
from screen.screen import Screen


class SelectScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        self.components.append(WrapImage("levelSelect",4))

        def on_click(level):
            def new():
                if globalvars.LEVELS_UNLOCKED>level:
                    globalvars.CURR_SCREEN = (globalvars.SCREEN_CONSTRS["level"]
                                              ((level_loader.load_level("level"+str(level+1)),)))
                    globalvars.CURR_LEVEL=level+1
            return new
        self.buttons = []
        self.scroll_offs=min(globalvars.LEVELS_UNLOCKED-1,14)
        self.vis_scroll_offs=self.scroll_offs
        for i in range(15):
            button = Button(75+i*40, 50, 27, 27, on_click(i))
            self.components.append(button)
            self.buttons.append(button)

        def scroll(amt):
            def new(): self.scroll_offs=min(14,max(0,self.scroll_offs+amt))
            return new
        self.components.append(Button(10, 50, 13, 27, scroll(-1)))
        self.components.append(Button(153, 50, 13, 27, scroll(1)))
        def back():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5,79,19,15, back))

    def render(self, screen: Surface):
        self.screen = screen
        screen.fill(pygame.Color(30,30,60))
        super().render(screen)

        self.vis_scroll_offs=self.vis_scroll_offs*0.9+self.scroll_offs*0.1
        for i in range(15):
            self.buttons[i].x = 75+i*40-self.vis_scroll_offs*40
            if abs(i-self.vis_scroll_offs)>1.3:
                self.buttons[i].y = 100
            else:
                self.buttons[i].y = 50
                self.screen.blit(globalvars.IMAGES["buttons"], (self.buttons[i].x, 50),
                                 ((i % 5) * 27, math.floor(i / 5) * 27, 27, 27))
                if globalvars.LEVELS_UNLOCKED<=i:
                    self.screen.blit(globalvars.IMAGES["buttons"], (self.buttons[i].x, 50),
                                     (81, 81, 27, 27))

        self.screen.blit(globalvars.IMAGES["buttons"], (10,50), (108, 81, 13, 27))
        self.screen.blit(globalvars.IMAGES["buttons"], (153,50), (122, 81, 13, 27))
        self.screen.blit(globalvars.IMAGES["buttons"], (5,79), (29,110, 19,15))
