import pygame

import level
import level_loader
from entity import disk, player, solid, spawn, tiles
import audio

audio

disk.init()
player.init()
solid.init()
spawn.init()
tiles.init()

# pygame setup
pygame.init()
SCREEN = None
clock = pygame.time.Clock()
running = True
dt = 0
def set_size(size):
    global SCREEN
    level.PIXEL_WIDTH=size
    SCREEN = pygame.display.set_mode((level.PIXEL_WIDTH * 11 * 16, level.PIXEL_WIDTH * 11 * 9))
set_size(7)

test_level = level_loader.load_level("test_level")

audio.title()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test_level.set_screen_size(SCREEN)

    test_level.tick()

    test_level.render(SCREEN)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()