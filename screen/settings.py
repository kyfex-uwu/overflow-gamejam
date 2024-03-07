import pygame.mouse

import audio
import globalvars
from screen.component.button import Button
from screen.component.component import Component
from screen.component.wrap_img import WrapImage
from screen.screen import Screen


class Slider(Component):
    def __init__(self, x, y, w, h, x_min, x_max, on_drag):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_min = x_min
        self.x_max = x_max
        self.on_drag = on_drag

    def render(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        x_pos = mouse_pos[0] / globalvars.PIXEL_WIDTH
        y_pos = mouse_pos[1] / globalvars.PIXEL_WIDTH

        if (pygame.mouse.get_pressed(3)[0] and
                self.x_min <= x_pos <= self.x_max + self.w and self.y <= y_pos <= self.y + self.h):
            self.x = max(self.x_min, min(self.x_max, x_pos - self.w / 2))
            self.on_drag()


class SettingsScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)

        self.components.append(WrapImage("settings", 3))

        def back():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5, 79, 19, 15, back))

        def slider():
            val = max(0, min(1, (self.vol_slider.x - 50) / 67))
            audio.music_vol(val)
            globalvars.CONFIG["volume"] = val
        self.vol_slider = Slider(50 + audio.music_vol(None) * 66, 50, 9, 9, 50, 117, slider)
        self.components.append(self.vol_slider)

        def screen_size():
            globalvars.set_size(round(max(0,min(8,((pygame.mouse.get_pos()[0]/globalvars.PIXEL_WIDTH-50)/75*8))))+1)
        self.size_slider = Button(50, 64, 75, 9, screen_size)
        self.components.append(self.size_slider)

        def credits():
            globalvars.CURR_SCREEN=globalvars.SCREEN_CONSTRS["credits"](())
        self.components.append(Button(123, 78, 50, 18, credits))

    def render(self, screen):
        screen.fill((30, 30, 60))

        super().render(screen)
        screen.blit(globalvars.IMAGES["buttons"], (5, 79), (26, 108, 19, 15))
        screen.blit(globalvars.IMAGES["buttons"], (123, 78), (45, 108, 50, 18))

        screen.blit(globalvars.IMAGES["buttons"], (35, 50), (0, 117, 13, 9))
        screen.blit(globalvars.IMAGES["buttons"], (35, 65), (13, 117, 13, 9))

        screen.blit(globalvars.IMAGES["buttons"], (52, 52), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121, 52), (13, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (52, 67), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121, 67), (13, 110, 3, 5))
        for i in range(55, 121):
            screen.blit(globalvars.IMAGES["buttons"], (i, 52), (12, 110, 1, 5))
            screen.blit(globalvars.IMAGES["buttons"], (i, 67), (12, 110, 1, 5))

        screen.blit(globalvars.IMAGES["buttons"], (self.vol_slider.x, 50), (0, 108, 9, 9))
        screen.blit(globalvars.IMAGES["buttons"], (50+(globalvars.PIXEL_WIDTH-1)*66/8, 65), (0, 108, 9, 9))
