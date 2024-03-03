import math
import os

import pygame
from pygame import Surface

import audio
import globalvars
import level_loader
from screen.component.button import Button
from screen.level import LevelScreen
from screen.screen import Screen


class SelectScreen(Screen):
    IMAGE = None
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        def on_click(level):
            globalvars.CURR_SCREEN = LevelScreen((level_loader.load_level(level),))
        self.components.append(Button(10,40,25,25, on_click, self, 1))
        self.components.append(Button(40,40,25,25, on_click, self, 2))
        self.components.append(Button(10,70,25,25, on_click, self, 3))
        self.components.append(Button(40,70,25,25, on_click, self, 4))

        if SelectScreen.IMAGE is None:
            SelectScreen.IMAGE = pygame.image.load(os.path.join('resources', 'levelSelect.png')).convert_alpha()

    def render(self, screen: Surface):
        self.screen = screen
        screen.fill(pygame.Color(30,30,60))
        super().render(screen)
        self.wrap_amt = (self.wrap_amt+0.015)%(math.pi*2)
        amt = round(math.sin(self.wrap_amt)*8+2)
        screen.blit(SelectScreen.IMAGE,(0,3), (2-amt,0,176,37))
        screen.blit(SelectScreen.IMAGE,(amt-10,3), (169,0,5,37))
        screen.blit(SelectScreen.IMAGE,(175+amt,3), (0,0,7,37))
