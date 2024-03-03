import pygame
from pygame import Surface

import level
import level_loader
import audio
from screen.level import LevelScreen
from screen.title import TitleScreen

# pygame setup
pygame.init()
SCREEN = None
SMALL_SCREEN = Surface((11*16, 11*9))
clock = pygame.time.Clock()
running = True
dt = 0


def set_size(size):
    global SCREEN
    level.PIXEL_WIDTH = size
    SCREEN = pygame.display.set_mode((level.PIXEL_WIDTH * 11 * 16, level.PIXEL_WIDTH * 11 * 9))
set_size(7)

from entity import disk, player, solid, spawn, tiles, spikes
for entity in {disk, player, solid, spawn, tiles, spikes}:
    entity.init()
test_level = level_loader.load_level("test_level")

CURR_SCREEN = LevelScreen((test_level,))

audio.title()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CURR_SCREEN.render(SMALL_SCREEN)
    pygame.transform.scale(SMALL_SCREEN, SCREEN.get_size(), SCREEN)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
