import pygame

import level_loader
from entity import disk, player, solid, spawn, tiles

disk.init()
player.init()
solid.init()
spawn.init()
tiles.init()

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = level_loader.load_level("test_level")
print(test_level.entities)

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