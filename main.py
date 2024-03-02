import math

import pygame

from entity.player import PlayerEntity
from entity.solid import SolidEntity
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(70,30)
SolidEntity(24,14.800003051757812,14,23,(50,50,70)).init(test_level)
SolidEntity(48,16.800003051757812,14,26,(50,50,70)).init(test_level)
SolidEntity(8,52.80000305175781,10,30,(50,50,70)).init(test_level)
SolidEntity(19,82.80000305175781,51,13,(50,50,70)).init(test_level)
SolidEntity(70,53.80000305175781,11,27,(50,50,70)).init(test_level)
SolidEntity(33,49.80000305175781,20,6,(50,50,70)).init(test_level)
SolidEntity(36,54.80000305175781,14,5,(50,50,70)).init(test_level)
SolidEntity(35,-10.199996948242188,0,0,(50,50,70)).init(test_level)
test_entity2 = PlayerEntity(50, 50, 8,8,(30,40,50))
test_entity2.init(test_level)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test_level.set_screen_size(SCREEN)

    test_level.tick()

    test_level.render(SCREEN)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    test_entity2.rcolor += round(math.sin(test_entity2.bcolor))
    test_entity2.bcolor += round(math.sin(test_entity2.gcolor))
    test_entity2.gcolor += round(math.sin(test_entity2.rcolor + 1))
pygame.quit()