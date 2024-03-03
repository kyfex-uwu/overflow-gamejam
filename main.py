import pygame
import os
from pygame import mixer

import level_loader
from entity import disk, player, solid, spawn, tiles

disk.init()
player.init()
solid.init()
spawn.init()
tiles.init()

# pygame setup
pygame.init()
mixer.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = level_loader.load_level("test_level")
print(test_level.entities)

#music
#channel 1 is for main music
#channel 2 is for sound effects
mixer.Channel(1)
mixer.Channel(2)
mainTheme = mixer.Sound(os.path.join("resources", "audio", "Platforms-in-the-Sky.ogg"))
levelComplete = mixer.Sound(os.path.join("resources", "audio", "Level-Complete.ogg"))
mixer.Channel(1).play(mainTheme, loops= -1)
#mixer.Channel(2).play(levelComplete)

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