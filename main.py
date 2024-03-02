import pygame

from entity.player import PlayerEntity
from entity.solid import SolidEntity
from entity.spawn import SpawnPointEntity
from entity.tiles import Tiles
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(32,18)
PlayerEntity(10,10).init(test_level)

SpawnPointEntity(80,24,15,14,(87.5,31)).init(test_level)

Tiles({
    "A": (0,0,"test")
},"""


.A
..A............AAA
..A..........A...A
...A......AA.....A
....A.....A......A
......AA.........A
.........A""").init(test_level)

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