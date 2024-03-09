import math
import os

import pygame
from pygame import Surface

import globalvars
import keys
from screen.component.button import Button
from screen.screen import Screen
import audio

def drawNum(num, x, y, screen): # : 10, . 11
    screen.blit(LevelScreen.NUMBERS, (x, y), (num*3, 0, 3, 5))

def drawTimer(time, screen, color):
    pygame.draw.rect(screen, color, (137, 0, 39, 7))

    drawNum(time % 10, 172, 1, screen)
    time = math.floor(time / 10)
    drawNum(time % 10, 168, 1, screen)
    time = math.floor(time / 10)
    drawNum(time % 10, 164, 1, screen)
    time = math.floor(time / 10)
    drawNum(11, 161, 1, screen)
    drawNum(time % 10, 158, 1, screen)
    time = math.floor(time / 10)
    drawNum(time % 6, 154, 1, screen)
    time = math.floor(time / 6)
    drawNum(10, 151, 1, screen)
    drawNum(time % 10, 148, 1, screen)
    time = math.floor(time / 10)
    drawNum(time % 6, 144, 1, screen)
    time = math.floor(time / 6)
    drawNum(10, 141, 1, screen)
    drawNum(time % 10, 138, 1, screen)

    x_pos = 138
    while time > 0:
        time = math.floor(time / 10)
        if time < 1: break
        x_pos -= 4
        pygame.draw.rect(screen, color, (x_pos - 1, 0, 4, 7))
        drawNum(time % 10, x_pos, 1, screen)

class LevelScreen(Screen):
    NUMBERS=None
    PAUSE_OVERLAY = None
    def __init__(self, args):
        super().__init__(args)
        self.level = args[0]
        
        if globalvars.CURR_LEVEL <= 15:
            audio.playLevel()
        else:
            audio.glitched()     

        def on_click():
            if self.paused:
                globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["select"](
                    (globalvars.CURR_LEVEL-1,globalvars.CURR_LEVEL-1))
                globalvars.CURR_LEVEL=-1
        self.components.append(Button(65, 39, 40, 20, on_click))

        self.paused=False

        if LevelScreen.NUMBERS is None:
            LevelScreen.NUMBERS = pygame.image.load(os.path.join('resources', 'numbers.png'))
        if LevelScreen.PAUSE_OVERLAY is None:
            LevelScreen.PAUSE_OVERLAY = Surface((176,99), flags=pygame.SRCALPHA)
            LevelScreen.PAUSE_OVERLAY.fill((0,0,0, 100))

    def render(self, screen):
        if keys.PAUSE.pressed:
            self.paused = not self.paused

        if not self.paused:
            self.level.tick()
        self.level.render(screen)
        if self.paused:
            screen.blit(LevelScreen.PAUSE_OVERLAY, (0,0), )
            screen.blit(globalvars.IMAGES["buttons"], (65, 39), (95,108, 40,20))

        super().render(screen)

        time=round(globalvars.TIMER * 1000)
        color=(0, 200, 0) if self.level.finished else (100, 100, 100)
        drawTimer(time, screen, color)
