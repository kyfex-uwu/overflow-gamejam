import math
import os

import pygame
from pygame import Surface

import globalvars
from entity.entity import Vector

PIXEL_WIDTH=8

def drawNum(num, x, y, screen): # : 10, . 11
    screen.blit(Level.NUMBERS, (x, y), (num*3, 0, 3, 5))

class Level:
    NUMBERS=None
    def __init__(self, w, h): # in tiles
        self.w=max(22,w)
        self.h=max(18,h)
        self.x=0
        self.y=0
        self.xVel=0
        self.surface = Surface((self.w*8,self.h*8), flags=pygame.SRCALPHA)
        self.screenSize=Vector(11*16,11*9)

        self.entities = []
        self.default_spawn = None
        self.player_entity = None

        self.finished = False

        if Level.NUMBERS is None:
            Level.NUMBERS = pygame.image.load(os.path.join('resources', 'numbers.png'))

    def render(self, dest: Surface):
        self.x = max(0, min(self.w * 8 - self.screenSize.x, self.x + self.xVel))
        self.y = max(0, min(self.h * 8 - self.screenSize.y, self.y))
        self.surface.fill(pygame.Color(30,30,60))

        for entity in self.entities:
            entity.render()

        pygame.draw.rect(self.surface, (0,0,0), (self.x+self.screenSize.x-39, self.y, 39, 7))

        time=round(globalvars.TIMER*1000)*9999
        drawNum(time%10, self.x+self.screenSize.x-4, self.y+1, self.surface)
        time=math.floor(time/10)
        drawNum(time%10, self.x+self.screenSize.x-8, self.y+1, self.surface)
        time=math.floor(time/10)
        drawNum(time%10, self.x+self.screenSize.x-12, self.y+1, self.surface)
        time=math.floor(time/10)
        drawNum(11, self.x+self.screenSize.x-15, self.y+1, self.surface)
        drawNum(time%10, self.x+self.screenSize.x-18, self.y+1, self.surface)
        time=math.floor(time/10)
        drawNum(time%6, self.x+self.screenSize.x-22, self.y+1, self.surface)
        time=math.floor(time/6)
        drawNum(10, self.x+self.screenSize.x-25, self.y+1, self.surface)
        drawNum(time%10, self.x+self.screenSize.x-28, self.y+1, self.surface)
        time=math.floor(time/10)
        drawNum(time%6, self.x+self.screenSize.x-32, self.y+1, self.surface)
        time=math.floor(time/6)
        drawNum(10, self.x+self.screenSize.x-35, self.y+1, self.surface)
        drawNum(time%10, self.x+self.screenSize.x-38, self.y+1, self.surface)

        x_pos = 38
        while time>0:
            time=math.floor(time/10)
            if time<1: break
            x_pos+=4
            pygame.draw.rect(self.surface, (0,0,0), (self.x+self.screenSize.x-x_pos-1, self.y, 4, 7))
            drawNum(time%10, self.x+self.screenSize.x-x_pos, self.y+1, self.surface)


        dest.blit(self.surface, (-self.x, -self.y,self.screenSize.x,self.screenSize.y))

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.xVel = min(self.xVel + 0.4, 2)
        if keys[pygame.K_LEFT]:
            self.xVel = max(self.xVel - 0.4, -2)

        self.xVel *= 0.8

        if self.player_entity is not None:
            self.y = self.y * 0.9 + (self.player_entity.y - self.screenSize.y / 5 * 3) * 0.1

        self.entities.sort(key=lambda e: e.z)
        for entity in self.entities:
            entity.tick()
