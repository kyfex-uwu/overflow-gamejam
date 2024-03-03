import pygame
import os

import level_loader
from entity.gravity import GravityEntity
import audio


class PlayerEntity(GravityEntity):
    IMAGE = None
    def __init__(self):
        super().__init__(0,0, 6, 6)
        self.z=10
        self.is_jumping=0
        self.spawnpoint = (0,0)

        if PlayerEntity.IMAGE is None:
            PlayerEntity.IMAGE = pygame.image.load(os.path.join('resources', 'player.png')).convert_alpha()

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

            self.yVel -= 1.7*self.is_jumping/10
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

        self.parse=(12,0,6,6)
        
        if self.xVel >= 1:
            self.parse=(0,0,6,6)
        elif self.xVel <= -1:
            self.parse=(6,0,6,6)
        elif self.yVel < 0:
            self.parse=(0,6,0,0)
        elif self.is_jumping :
            self.parse=(6,6,6,6)

    def kill(self):
        audio.hurt()
        self.x = self.spawnpoint[0]
        self.y = self.spawnpoint[1]

    def render(self, image="spikes"):
        self.level.surface.blit(PlayerEntity.IMAGE, (self.x, self.y), self.parse)

def init():
    level_loader.ENTITY_LOADERS['player'] = lambda strings: PlayerEntity()