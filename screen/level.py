import math
import os

import pygame

import globalvars
from screen.screen import Screen
import audio

def drawNum(num, x, y, screen): # : 10, . 11
    screen.blit(LevelScreen.NUMBERS, (x, y), (num*3, 0, 3, 5))

class LevelScreen(Screen):
    NUMBERS=None
    def __init__(self, args):
        super().__init__(args)
        self.level = args[0]
        audio.playLevel()

        if LevelScreen.NUMBERS is None:
            LevelScreen.NUMBERS = pygame.image.load(os.path.join('resources', 'numbers.png'))
    def render(self, screen):
        self.level.tick()
        self.level.render(screen)

        color = (0, 200, 0) if self.level.finished else (100, 100, 100)
        pygame.draw.rect(screen, color, (137,0, 39, 7))

        time = round(globalvars.TIMER * 1000)
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
            pygame.draw.rect(screen, color, (x_pos-1, 0, 4, 7))
            drawNum(time % 10, x_pos, 1, screen)
