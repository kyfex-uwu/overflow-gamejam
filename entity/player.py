import pygame

from entity.gravity import GravityEntity


class PlayerEntity(GravityEntity):
    def __init__(self):
        super().__init__(0,0, 6, 6)
        self.is_jumping=0
        self.spawnpoint = (0,0)

    def init(self, level):
        super().init(level)
        level.player_entity = self
        if level.default_spawn is not None:
            self.spawnpoint = level.default_spawn
            self.x=self.spawnpoint[0]
            self.y=self.spawnpoint[1]

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and (self.normal.y==-1 or self.is_jumping > 0):
            if self.is_jumping == 0: self.is_jumping = 10
            self.is_jumping -= 1

            self.yVel -= 3
        else:
            self.is_jumping = 0
        if self.normal.y==1:
            self.is_jumping=-1

        if keys[pygame.K_a]:
            self.xVel = max(self.xVel - 0.5, -2)
        if keys[pygame.K_d]:
            self.xVel = min(self.xVel + 0.5, 2)
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.xVel *= 0.7

        if self.x+self.w < self.level.x:
            self.x = self.level.x+self.level.screenSize.x
        elif self.x > self.level.x+self.level.screenSize.x:
            self.x = self.level.x-self.w
        if self.y+self.h > self.level.y + self.level.h*8:
            self.kill()

        super().tick()

    def kill(self):
        self.x = self.spawnpoint[0]
        self.y = self.spawnpoint[1]