import pygame

from entity.solid import SolidEntity


class GravityEntity(SolidEntity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.is_jumping=0

    def tick(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and (self.grounded or self.is_jumping>0):
            if self.is_jumping == 0: self.is_jumping=10
            self.is_jumping -= 1

            self.yVel = max(self.yVel-3,-5)
        else: self.is_jumping=0
        if keys[pygame.K_a]:
            self.xVel -= 1
        if keys[pygame.K_d]:
            self.xVel += 1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.xVel *= 0.7

        self.xVel = (1 if self.xVel>=0 else -1) * min(abs(self.xVel), 3)

        self.yVel += 0.5
        super().tick()
