import pygame

from entity.player import PlayerEntity
from entity.solid import SolidEntity
from entity.tiles import Tiles
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(64,18)
PlayerEntity(10,10,10,10).init(test_level)

Tiles({
    "A": (4,2,"test"),
    "B": (2,0,"test"),
    "C": (3,4,"test"),
    "D": (2,4,"test"),
    "E": (5,2,"test"),
    "F": (0,2,"test"),
    "G": (1,2,"test"),
    "H": (3,2,"test"),
    "I": (3,3,"test"),
    "J": (5,3,"test"),
    "K": (3,1,"test"),
    "L": (3,5,"test"),
    "M": (5,1,"test"),
    "N": (4,3,"test"),
    "O": (2,5,"test")
},"""
ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBE
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
F..............................GH..............................F
NBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBLOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBJ""").init(test_level)

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