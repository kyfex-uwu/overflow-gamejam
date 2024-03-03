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
    BUTTON_IMG = None
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        def on_click(level):
            def new():
                globalvars.CURR_SCREEN = LevelScreen((level_loader.load_level(level),))
            return new
        self.components.append(Button(10,40,9, 9, on_click("level1")))
        self.components.append(Button(40,40,9, 9, on_click("k_level1")))
        self.components.append(Button(10,70,9, 9, on_click("level3")))
        self.components.append(Button(40,70,9, 9, on_click("level4")))

        if SelectScreen.IMAGE is None:
            SelectScreen.IMAGE = pygame.image.load(os.path.join('resources', 'levelSelect.png')).convert_alpha()
        if SelectScreen.BUTTON_IMG is None:
            SelectScreen.BUTTON_IMG = pygame.image.load(os.path.join('resources', 'buttons.png')).convert_alpha()

    def render(self, screen: Surface):
        self.screen = screen
        screen.fill(pygame.Color(30,30,60))
        super().render(screen)
        self.wrap_amt = (self.wrap_amt+0.015)%(math.pi*2)
        amt = round(math.sin(self.wrap_amt)*8+4)
        screen.blit(SelectScreen.IMAGE,(0,3), (2-amt,0,176,37))
        screen.blit(SelectScreen.IMAGE,(amt-12,3), (167,0,5,37))
        screen.blit(SelectScreen.IMAGE,(175+amt,3), (0,0,5,37))

        self.screen.blit(SelectScreen.BUTTON_IMG, (10,40), (0, 0, 9, 9))
        self.screen.blit(SelectScreen.BUTTON_IMG, (40,40), (9, 0, 9, 9))
        self.screen.blit(SelectScreen.BUTTON_IMG, (10,70), (18,0, 9, 9))
        self.screen.blit(SelectScreen.BUTTON_IMG, (40,70), (27, 0, 9, 9))
