import os

import pygame

import globalvars
from screen.component.button import Button
from screen.screen import Screen


class CreditsScreen(Screen):
    IMAGE = None
    def __init__(self, args: tuple):
        super().__init__(args)

        def back():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5, 79, 19, 15, back))

        if CreditsScreen.IMAGE is None:
            CreditsScreen.IMAGE = pygame.image.load(os.path.join('resources', '../resources/credits.png'))

    def render(self, screen):
        screen.fill((30, 30, 60))

        super().render(screen)

        screen.blit(globalvars.IMAGES["buttons"], (5, 79), (26, 108, 19, 15))
        screen.blit(CreditsScreen.IMAGE, (24, 5))
