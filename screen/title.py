import pygame
from pygame import Surface

from screen.screen import Screen


class TitleScreen(Screen):
    def render(self, screen: Surface):
        screen.fill(pygame.Color(30,30,60))
        screen.blit(pygame.font.SysFont(pygame.font.get_default_font(),32).render(
            "test", True, (255,255,255)),(10,10))