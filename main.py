import pygame
from pygame import Surface

import globalvars
import level_loader
import audio
from screen.level import LevelScreen
from screen.title import TitleScreen

# pygame setup
pygame.init()
SCREEN = None
SMALL_SCREEN = Surface((11*16, 11*9))
LEVELS_UNLOCKED = 1
clock = pygame.time.Clock()
running = True
dt = 0


def set_size(size):
    global SCREEN
    globalvars.PIXEL_WIDTH = size
    SCREEN = pygame.display.set_mode((globalvars.PIXEL_WIDTH * 11 * 16, globalvars.PIXEL_WIDTH * 11 * 9))

#window size
set_size(7)

from entity import disk, player, solid, spawn, tiles, spikes, display
for entity in {disk, player, solid, spawn, tiles, spikes, display}:
    entity.init()

globalvars.CURR_SCREEN = TitleScreen(())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    globalvars.MOUSE["p_left"] = globalvars.MOUSE["left"]
    globalvars.MOUSE["p_right"] = globalvars.MOUSE["right"]
    state = pygame.mouse.get_pressed(3)
    globalvars.MOUSE["left"] = state[0]
    globalvars.MOUSE["right"] = state[2]

    if isinstance(globalvars.CURR_SCREEN, LevelScreen) and not globalvars.CURR_SCREEN.level.finished:
        globalvars.TIMER+=dt

    globalvars.CURR_SCREEN.render(SMALL_SCREEN)
    pygame.transform.scale(SMALL_SCREEN, SCREEN.get_size(), SCREEN)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
