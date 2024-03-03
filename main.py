import pygame
import os
from pygame import mixer

from entity.disk import DiskEntity
from entity.player import PlayerEntity
from entity.solid import SolidEntity
from entity.spawn import SpawnPointEntity
from entity.tiles import Tiles
from level import Level
from entity.spikes import SpikeEntity

# pygame setup
pygame.init()
mixer.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0




test_level = Level(11,11)
PlayerEntity().init(test_level)

SpawnPointEntity(1,7,38,14,(17,11)).init(test_level)
SpawnPointEntity(17,33,24,14,(26,37)).init(test_level)
SpikeEntity(76.5,40.5,"up").init(test_level)
SpikeEntity(47.5,31.75,"down").init(test_level)
SpikeEntity(0,72.5,"up").init(test_level)
SpikeEntity(-40,26,"right").init(test_level)
DiskEntity(61,74).init(test_level)
DiskEntity(62,73).init(test_level)
DiskEntity(-79,2).init(test_level)

Tiles({
    "A": (7,5,"blueTiles"),
    "B": (1,0,"blueTiles"),
    "C": (2,0,"blueTiles"),
    "D": (3,0,"blueTiles")
},"""

..........A

BCCCCCD


..BCCCCCCCD



BCCCCCCCD""").init(test_level)

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