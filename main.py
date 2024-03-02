import pygame

from entity.disk import DiskEntity
from entity.player import PlayerEntity
from entity.solid import SolidEntity
from entity.spawn import SpawnPointEntity
from entity.tiles import Tiles
from level import Level
from entity.spikes import SpikeEntity

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


test_level = Level(25,19)
PlayerEntity().init(test_level)

SpawnPointEntity(1,1,28,20,(15,11)).init(test_level)
SpawnPointEntity(71,45,14,16,(78,53)).init(test_level)
SolidEntity(41,89,6,6).init(test_level)
SpawnPointEntity(77,91,20,16,(87,99)).init(test_level)
DiskEntity(77,91).init(test_level)
SpikeEntity(50, 50, "up").init(test_level)
SpikeEntity(10, 10, "down").init(test_level)
SpikeEntity(20, 20, "left").init(test_level)
SpikeEntity(30, 30, "right").init(test_level)

Tiles({
    "A": (0,1,"blueTiles"),
    "B": (1,0,"blueTiles"),
    "C": (3,0,"blueTiles"),
    "D": (0,2,"blueTiles"),
    "E": (2,0,"blueTiles"),
    "F": (5,3,"blueTiles"),
    "G": (4,2,"blueTiles"),
    "H": (5,1,"blueTiles"),
    "I": (5,2,"blueTiles"),
    "J": (5,0,"blueTiles"),
    "K": (4,1,"blueTiles"),
    "L": (7,5,"blueTiles"),
    "M": (4,3,"blueTiles"),
    "N": (4,0,"blueTiles"),
    "O": (7,5,"test2"),
    "P": (0,3,"blueTiles"),
    "Q": (1,0,"test2"),
    "R": (2,0,"test2"),
    "S": (3,0,"test2")
},"""

.........A
.BC......D
....BEEC.D
.........D
.......BEF

......BEEEC

.....A
....GHI
...BJ.KC
...LMNF.......O
.....P...QRRRRRS
...................


.........................
.......................R""").init(test_level)

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