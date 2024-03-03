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
from screen.select import SelectScreen


class TitleScreen(Screen):
    IMAGE = None
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        def on_click():
            globalvars.CURR_SCREEN = SelectScreen(())
        self.components.append(Button(58,50,60,30, on_click, self))

        if TitleScreen.IMAGE is None:
            TitleScreen.IMAGE = pygame.image.load(os.path.join('resources', 'title.png')).convert_alpha()

    def render(self, screen: Surface):
        self.screen = screen
        screen.fill(pygame.Color(30,30,60))
        super().render(screen)
        self.wrap_amt = (self.wrap_amt+0.015)%(math.pi*2)
        amt = round(math.sin(self.wrap_amt)*8+2)
        screen.blit(TitleScreen.IMAGE,(0,3), (2-amt,0,176,33))
        screen.blit(TitleScreen.IMAGE,(amt-10,3), (169,0,5,33))
        screen.blit(TitleScreen.IMAGE,(175+amt,3), (0,0,7,33))

