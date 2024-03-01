import pygame

from entity import Entity
from level import Level

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

test_level = Level(400,30)
test_entity = Entity(10, 50, 30, 70)
test_entity.init(test_level)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test_level.tick()

    vfactor = 300

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and test_level.y - vfactor*dt >= 0:
        test_level.y -= vfactor * dt
    if keys[pygame.K_s] and test_level.y - vfactor*dt <= test_level.h:
        test_level.y += vfactor * dt
    if keys[pygame.K_a] and test_level.x - vfactor*dt >= 0:
        test_level.x -= vfactor * dt
    if keys[pygame.K_d] and test_level.y - vfactor*dt <= test_level.w:
        test_level.x += vfactor * dt

    test_level.render(SCREEN)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()