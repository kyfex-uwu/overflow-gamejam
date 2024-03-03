import pygame.mouse

from screen.component.component import SizedComponent


class Button(SizedComponent):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
    def render(self, screen):
        super().render(screen)
        if pygame.mouse.get_pos()[0] <= x and pygame.mouse.get_pos()[0] >= x+w:
            pass