from inspect import getmembers

import pygame.mouse

import audio
import font
import globalvars
import keys
from screen.component.button import Button
from screen.component.component import Component
from screen.component.wrap_img import WrapImage
from screen.level import drawTimer
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

def get_vis_pos(vis_slide):
    if vis_slide<=1: return (vis_slide, 0)
    else: return (1, vis_slide-1)

class SettingsScreen(Screen):
    _MEMBERS = None
    def __init__(self, args: tuple):
        super().__init__(args)
        self.slide = 0
        self.vis_slide = 0

        self.key_buttons = []
        self.setting_key = None

        self.components.append(WrapImage("settings", 3))

        if SettingsScreen._MEMBERS is None:
            SettingsScreen._MEMBERS = getmembers(pygame.constants)

        def back():
            if self.setting_key is not None: return
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5, 79, 19, 15, back))

        orig_key_ys = []
        def slide_change(val):
            def new():
                if self.setting_key is not None: return
                self.slide = max(-1, min(2, self.slide + val))
                if self.slide == 2:
                    for i in range(len(self.key_buttons)): self.key_buttons[i][1].y=orig_key_ys[i]-50
                else:
                    for i in range(len(self.key_buttons)): self.key_buttons[i][1].y=orig_key_ys[i]
            return new
        self.components.append(Button(5, 41, 13, 27, slide_change(-1)))
        self.components.append(Button(158, 41, 13, 27, slide_change(1)))

        #####

        def reset():
            if self.vis_slide != -1: return
            globalvars.LEVELS_UNLOCKED = 1
            globalvars.CURR_LEVEL = -1
            globalvars.FINISHED = False
            globalvars.TIMER = 0
        self.components.append(Button(66,55,43,18,reset))

        #####

        def slider():
            if self.vis_slide != 0: return

            val = max(0, min(1, (self.vol_slider.x - 50) / 67))
            audio.music_vol(val)
            audio.sfx_vol(val)
            globalvars.CONFIG["volume"] = val

        self.vol_slider = Slider(50 + audio.music_vol(None) * 66, 46, 9, 9, 50, 117, slider)
        self.components.append(self.vol_slider)

        def screen_size():
            if self.vis_slide != 0: return
            globalvars.set_size(
                round(max(0, min(8, ((pygame.mouse.get_pos()[0] / globalvars.PIXEL_WIDTH - 50) / 75 * 8)))) + 1)

        self.size_slider = Button(50, 60, 75, 9, screen_size)
        self.components.append(self.size_slider)

        def credits():
            if self.vis_slide != 0: return
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["credits"](())

        self.components.append(Button(123, 78, 50, 18, credits))

        #####

        def change_key(data):
            def new():
                if not (1<=self.vis_slide<=3) or self.setting_key is not None: return
                self.setting_key = data
            return new
        for i in range(len(keys.all_keys)):
            data = keys.all_keys[i]
            if data.name == "": break
            length = len(data.name + ": " + pygame.key.name(data.key)) * 6
            data = (data, Button(88 - length / 2, 40 + i * 10, length, 10, change_key(data)))
            self.key_buttons.append(data)
            self.components.append(data[1])
        for data in self.key_buttons: orig_key_ys.append(data[1].y)

    def render(self, screen):
        self.vis_slide = round((self.slide * 0.1 + self.vis_slide * 0.9) * 1000) / 1000
        if abs(self.vis_slide - self.slide) < 0.006: self.vis_slide = self.slide

        screen.fill((30, 30, 60))
        super().render(screen)

        vis_pos = get_vis_pos(self.vis_slide)

        #####

        screen.blit(globalvars.IMAGES["buttons"], (66 - (vis_pos[0]+1) * 176, 55), (0,126,43,18))
        drawTimer(round(globalvars.TIMER * 1000), screen, (0, 200, 0) if globalvars.FINISHED else (100, 100, 100),
                  88+21 - (vis_pos[0]+1)*176, 73)

        #####

        # slider icons
        screen.blit(globalvars.IMAGES["buttons"], (35 - vis_pos[0] * 176, 46), (0, 117, 13, 9))
        screen.blit(globalvars.IMAGES["buttons"], (35 - vis_pos[0] * 176, 61), (13, 117, 13, 9))

        # sliders
        screen.blit(globalvars.IMAGES["buttons"], (52 - vis_pos[0] * 176, 48), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121 - vis_pos[0] * 176, 48), (13, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (52 - vis_pos[0] * 176, 63), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121 - vis_pos[0] * 176, 63), (13, 110, 3, 5))
        for i in range(55, 121):
            screen.blit(globalvars.IMAGES["buttons"], (i - vis_pos[0] * 176, 48), (12, 110, 1, 5))
            screen.blit(globalvars.IMAGES["buttons"], (i - vis_pos[0] * 176, 63), (12, 110, 1, 5))

        screen.blit(globalvars.IMAGES["buttons"], (self.vol_slider.x - vis_pos[0] * 176, 46), (0, 108, 9, 9))
        screen.blit(globalvars.IMAGES["buttons"], (50 + (globalvars.PIXEL_WIDTH - 1) * 66 / 8 - vis_pos[0] * 176,
                                                   61), (0, 108, 9, 9))

        # credits
        screen.blit(globalvars.IMAGES["buttons"], (123 - self.vis_slide * 176, 78), (45, 108, 50, 18))

        #####

        for data in self.key_buttons:
            if data[0].name == "": break
            if data[1].y - (vis_pos[1]-(1 if self.slide>1 else 0))*50 < 35: continue
            font.write(screen, data[0].name + ": " + pygame.key.name(data[0].key), 88 - (vis_pos[0] - 1) * 176,
                       data[1].y - (vis_pos[1]-(1 if self.slide>1 else 0))*50, centered=1)

        #####

        # back
        screen.blit(globalvars.IMAGES["buttons"], (5, 79), (26, 108, 19, 15))

        # nav buttons
        if self.vis_slide > -0.5:
            screen.blit(globalvars.IMAGES["buttons"], (5, 41), (108, 81, 13, 27))
        if self.vis_slide < 1.5:
            screen.blit(globalvars.IMAGES["buttons"], (158, 41), (122, 81, 13, 27))

        # keys overlay
        if self.setting_key is not None:
            screen.fill((70, 70, 70), special_flags=pygame.BLEND_MULT)
            font.write(screen, "Press new\n" + self.setting_key.name + " key", 88, 45, centered=1)
            pressed_keys = pygame.key.get_pressed()
            for name, val in SettingsScreen._MEMBERS:
                if isinstance(val, int) and pressed_keys[val]:
                    self.setting_key.key = val
                    self.setting_key = None
                    break
