import pygame
from pygame import Surface

from screen.component.button import Button
from screen.screen import Screen


class TitleScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)
        self.components.append(Button(2,2,10,5))

    def render(self, screen: Surface):
        screen.fill(pygame.Color(30,30,60))
        super().render(screen)
        screen.blit(pygame.font.SysFont(pygame.font.get_default_font(),32).render(
            "test", True, (255,255,255)),(10,10))

