import pygame

from entity.entity import Entity
from entity.solid import SolidEntity
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(40,30)
test_entity = SolidEntity(5,120,200,5, 100)
test_entity.init(test_level)
test_entity2 = SolidEntity(50, 50, 8,8, 100)
test_entity2.init(test_level)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test_level.tick()

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    test_level.render(SCREEN)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()