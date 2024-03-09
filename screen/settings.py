import pygame.mouse

import audio
import font
import globalvars
import keys
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
        self.slide=0
        self.vis_slide=0
        self.keys_scroll=0

        self.components.append(WrapImage("settings", 3))

        def back():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5, 79, 19, 15, back))

        def slide_change(val):
            def new():
                self.slide=max(0,min(1,self.slide+val))
            return new
        self.components.append(Button(5, 41, 13, 27, slide_change(-1)))
        self.components.append(Button(158, 41, 13, 27, slide_change(1)))

        ###

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
            globalvars.set_size(round(max(0,min(8,((pygame.mouse.get_pos()[0]/globalvars.PIXEL_WIDTH-50)/75*8))))+1)
        self.size_slider = Button(50, 60, 75, 9, screen_size)
        self.components.append(self.size_slider)

        def credits():
            globalvars.CURR_SCREEN=globalvars.SCREEN_CONSTRS["credits"](())
        self.components.append(Button(123, 78, 50, 18, credits))

    def render(self, screen):
        self.vis_slide = round((self.slide*0.1+self.vis_slide*0.9)*1000)/1000

        screen.fill((30, 30, 60))
        super().render(screen)

        #####

        # slider icons
        screen.blit(globalvars.IMAGES["buttons"], (35-self.vis_slide*176, 46), (0, 117, 13, 9))
        screen.blit(globalvars.IMAGES["buttons"], (35-self.vis_slide*176, 61), (13, 117, 13, 9))

        # sliders
        screen.blit(globalvars.IMAGES["buttons"], (52-self.vis_slide*176, 48), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121-self.vis_slide*176, 48), (13, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (52-self.vis_slide*176, 63), (9, 110, 3, 5))
        screen.blit(globalvars.IMAGES["buttons"], (121-self.vis_slide*176, 63), (13, 110, 3, 5))
        for i in range(55, 121):
            screen.blit(globalvars.IMAGES["buttons"], (i-self.vis_slide*176, 48), (12, 110, 1, 5))
            screen.blit(globalvars.IMAGES["buttons"], (i-self.vis_slide*176, 63), (12, 110, 1, 5))

        screen.blit(globalvars.IMAGES["buttons"], (self.vol_slider.x-self.vis_slide*176, 46), (0, 108, 9, 9))
        screen.blit(globalvars.IMAGES["buttons"], (50+(globalvars.PIXEL_WIDTH-1)*66/8-self.vis_slide*176,
                                                   61), (0, 108, 9, 9))

        #####

        font.write(screen, "Left: "+pygame.key.name(keys.LEFT.key), 88-(self.vis_slide-1)*176, 40, centered=1)
        font.write(screen, "Right: "+pygame.key.name(keys.RIGHT.key), 88-(self.vis_slide-1)*176, 50, centered=1)
        font.write(screen, "Jump: "+pygame.key.name(keys.JUMP.key), 88-(self.vis_slide-1)*176, 60, centered=1)
        font.write(screen, "S Left: "+pygame.key.name(keys.SCR_LEFT.key), 88-(self.vis_slide-1)*176, 70, centered=1)
        font.write(screen, "S Right: "+pygame.key.name(keys.SCR_RIGHT.key), 88-(self.vis_slide-1)*176, 80, centered=1)
        font.write(screen, "Pause: "+pygame.key.name(keys.PAUSE.key), 88-(self.vis_slide-1)*176, 90, centered=1)

        #####

        # back
        screen.blit(globalvars.IMAGES["buttons"], (5, 79), (26, 108, 19, 15))

        # credits
        screen.blit(globalvars.IMAGES["buttons"], (123, 78), (45, 108, 50, 18))

        # nav buttons
        if self.vis_slide > 0.5:
            screen.blit(globalvars.IMAGES["buttons"], (5, 41), (108, 81, 13, 27))
        if self.vis_slide < 0.5:
            screen.blit(globalvars.IMAGES["buttons"], (158, 41), (122, 81, 13, 27))
