import pygame

from entity.gravity import GravityEntity
from entity.solid import SolidEntity
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(40,30)
SolidEntity(5,120,200,5).init(test_level) # wall 1
SolidEntity(5,50,5,70).init(test_level) # wall 2
SolidEntity(5,5,200,5).init(test_level) # wall 3
SolidEntity(50,50,5,70).init(test_level) # wall 4
test_entity2 = GravityEntity(50, 50, 8,8)
test_entity2.init(test_level)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test_level.tick()

    test_level.render(SCREEN)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()