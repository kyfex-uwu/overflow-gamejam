import pygame
from pygame import Surface

import audio
import globalvars
from screen.component.button import Button
from screen.component.wrap_img import WrapImage
from screen.level import drawTimer
from screen.screen import Screen


class TitleScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        self.components.append(WrapImage("title",2))

        def on_click():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["select"](
                (globalvars.LEVELS_UNLOCKED-1,globalvars.LEVELS_UNLOCKED-1))
        self.components.append(Button(75,50,27,27, on_click))
        def on_click2():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["settings"](())
        #self.components.append(Button(25,50,27,27, on_click2))

    def render(self, screen: Surface):
        self.screen = screen
        screen.fill((30,30,60))
        super().render(screen)

        self.screen.blit(globalvars.IMAGES["buttons"], (75,50), (27,81, 27, 27))
        #self.screen.blit(globalvars.IMAGES["buttons"], (25,50), (54,81, 27, 27))

        if globalvars.FINISHED is not False or True:
            drawTimer(round(globalvars.FINISHED * 1000), self.screen, (0, 200, 0))

