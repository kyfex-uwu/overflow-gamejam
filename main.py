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
SolidEntity(5,120,500,5,(100,0,100)).init(test_level) # wall 1
SolidEntity(5,50,5,70,(50,200,35)).init(test_level) # wall 2
SolidEntity(5,30,200,5,(20,80,230)).init(test_level) # wall 3
SolidEntity(50,70,5,70,(200,40,135)).init(test_level) # wall 4
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

pygame.quit()