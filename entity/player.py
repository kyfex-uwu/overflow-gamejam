import pygame

from entity.gravity import GravityEntity


class PlayerEntity(GravityEntity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.is_jumping=0

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and (self.grounded or self.is_jumping > 0):
            if self.is_jumping == 0: self.is_jumping = 10
            self.is_jumping -= 1

            self.yVel = max(self.yVel - 3, -5)
        else:
            self.is_jumping = 0
        if keys[pygame.K_a]:
            self.xVel -= 1
        if keys[pygame.K_d]:
            self.xVel += 1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.xVel *= 0.7

        if self.x+self.w < self.level.x:
            self.x = self.level.x+self.level.screenSize.x
        elif self.x > self.level.x+self.level.screenSize.x:
            self.x = self.level.x-self.w

        super().tick()