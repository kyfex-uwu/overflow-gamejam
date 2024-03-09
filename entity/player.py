import pygame
import os

import keys
import level_loader
from entity.gravity import GravityEntity
import audio
from entity.solid import SolidEntity

MAX_XVEL=1.7
X_ACCEL=0.4

class PlayerEntity(GravityEntity):
    IMAGE = None
    def __init__(self):
        super().__init__(0,0, 6, 6)
        self.z=10
        self.can_wrap=True
        self.is_jumping=0
        self.spawnpoint = (0,0)
        self.parse = (12,0,6,6)

        if PlayerEntity.IMAGE is None:
            PlayerEntity.IMAGE = pygame.image.load(os.path.join('resources', 'entity', 'player.png')).convert_alpha()

    def init(self, level):
        super().init(level)
        level.player_entity = self
        if level.default_spawn is not None:
            self.spawnpoint = level.default_spawn
            self.x=self.spawnpoint[0]
            self.y=self.spawnpoint[1]

    def tick(self):
        if keys.JUMP.pressed and self.normal.y==-1:
            self.is_jumping=15
        if self.is_jumping>0:
            if keys.JUMP.down:
                self.is_jumping -= 1
                self.yVel = self.yVel * 0.5 - 3 * max(0, self.is_jumping) / 15
            else:
                self.is_jumping=0
                self.yVel*=0.3

        if self.normal.y==1:
            self.is_jumping=-1

        self.parse=(12,0,6,6)
        if keys.LEFT.down:
            self.xVel = max(self.xVel - X_ACCEL, -MAX_XVEL)
            self.parse = (6, 0, 6, 6)
        if keys.RIGHT.down:
            self.xVel = min(self.xVel + X_ACCEL, MAX_XVEL)
            self.parse = (0, 0, 6, 6)
        if not keys.LEFT.down and not keys.RIGHT.down:
            self.xVel *= 0.7
        # if keys0[pygame.K_r]:
        #     self.kill()

        if not self.level.finished:
            if self.x+self.w < self.level.x:
                self.x += self.level.screenSize.x
            elif self.x > self.level.x+self.level.screenSize.x:
                self.x -= self.level.screenSize.x
        if self.y+self.h > self.level.y + self.level.h*8:
            self.kill()

        super().tick()

        if self.yVel < 0:
            self.parse=(6,6,6,6)
        elif self.yVel > 0:
            self.parse=(0,6,6,6)

    def kill(self):
        audio.hurt()
        self.x = self.spawnpoint[0]
        self.y = self.spawnpoint[1]
        self.xVel = 0
        self.yVel = 0
        #todo: change this!! some level reset something, camera is weird
        self.level.x = self.x+self.w/2-self.level.screenSize.x/2
        self.level.y = self.level.player_entity.y - self.level.screenSize.y / 5 * 3

    def render(self):
        self.level.surface.blit(PlayerEntity.IMAGE, (round(self.x), round(self.y)), self.parse)
        self.level.surface.blit(PlayerEntity.IMAGE, (round(self.x-self.level.screenSize.x), round(self.y)), self.parse)
        self.level.surface.blit(PlayerEntity.IMAGE, (round(self.x+self.level.screenSize.x), round(self.y)), self.parse)

        # for rect in self._collidables:
        #     pygame.draw.rect(self.level.surface, (255,0,0), (round(rect.x),round(rect.y),rect.w,rect.h))

def init():
    level_loader.ENTITY_LOADERS['player'] = lambda strings: PlayerEntity()