import pygame
import os

import level_loader
from entity.gravity import GravityEntity
import audio


MAX_XVEL=1.7
X_ACCEL=0.4

class PlayerEntity(GravityEntity):
    IMAGE = None
    def __init__(self):
        super().__init__(0,0, 6, 6)
        self.z=10
        self.is_jumping=0
        self.spawnpoint = (0,0)

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
        keys = pygame.key.get_pressed()
        cancel_jump=False
        if keys[pygame.K_w] and (self.normal.y==-1 or self.is_jumping > 0):
            if self.is_jumping == 0: self.is_jumping = 15
            self.is_jumping -= 1

            self.yVel = self.yVel*0.5-3*self.is_jumping/15
        else:
            cancel_jump=True
        if self.is_jumping>0 and keys[pygame.K_w] is False: self.yVel*=0.3
        if cancel_jump: self.is_jumping = 0

        if self.normal.y==1:
            self.is_jumping=-1

        if keys[pygame.K_a]:
            self.xVel = max(self.xVel - X_ACCEL, -MAX_XVEL)
        if keys[pygame.K_d]:
            self.xVel = min(self.xVel + X_ACCEL, MAX_XVEL)
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.xVel *= 0.7
        if keys[pygame.K_r]:
            self.kill()

        if not self.level.finished:
            if self.x+self.w < self.level.x:
                self.x += self.level.screenSize.x+self.w-1
            elif self.x > self.level.x+self.level.screenSize.x:
                self.x -= self.level.screenSize.x+self.w-1
        if self.y+self.h > self.level.y + self.level.h*8:
            self.kill()

        super().tick()

        self.parse=(12,0,6,6)
        
        if self.xVel >= 0.9:
            self.parse=(0,0,6,6)
        elif self.xVel <= -0.9:
            self.parse=(6,0,6,6)
        elif self.yVel < 0:
            self.parse=(6,6,6,6)
        elif self.yVel > 0:
            self.parse=(0,6,6,6)

    def kill(self):
        audio.hurt()
        self.x = self.spawnpoint[0]
        self.y = self.spawnpoint[1]
        self.xVel = 0
        self.yVel = 0
        self.level.x = self.x+self.w/2-self.level.screenSize.x/2
        self.level.y = self.level.player_entity.y - self.level.screenSize.y / 5 * 3

    def render(self, image="spikes"):
        self.level.surface.blit(PlayerEntity.IMAGE, (round(self.x), round(self.y)), self.parse)

def init():
    level_loader.ENTITY_LOADERS['player'] = lambda strings: PlayerEntity()