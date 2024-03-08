import pygame

import level_loader
from entity.entity import Entity, Vector, Rect

epsilon = 0.00001
inv_epsilon = 1 / epsilon


def isRayInRect(rayOrigin: Vector, rayDir: Vector, rect: Rect):
    tNear = Vector(
        (rect.x - rayOrigin.x) / rayDir.x,
        (rect.y - rayOrigin.y) / rayDir.y
    )
    tFar = Vector(
        (rect.x + rect.w - rayOrigin.x) / rayDir.x,
        (rect.y + rect.h - rayOrigin.y) / rayDir.y
    )

    if tNear.x > tFar.x:
        tNear.x, tFar.x = tFar.x, tNear.x
    if tNear.y > tFar.y:
        tNear.y, tFar.y = tFar.y, tNear.y
    if tNear.x > tFar.y or tNear.y > tFar.x:
        return False

    tHitNear = max(tNear.x, tNear.y)
    tHitFar = min(tFar.x, tFar.y)
    if tHitFar < 0 or tHitNear > 1:
        return False

    contactPoint = Vector(
        rayOrigin.x + tHitNear * rayDir.x,
        rayOrigin.y + tHitNear * rayDir.y
    )
    contactNormal = Vector(0, 0)
    if tNear.x > tNear.y:
        if rayDir.x < 0:
            contactNormal = Vector(1, 0)
        else:
            contactNormal = Vector(-1, 0)
    elif tNear.x < tNear.y:
        if rayDir.y < 0:
            contactNormal = Vector(0, 1)
        else:
            contactNormal = Vector(0, -1)
    return {
        'point': contactPoint,
        'normal': contactNormal,
        'distance': tHitNear
    }


class SolidEntity(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.normal = Vector(0, 0)
        self.solid = True
        self.can_wrap=False

    def tick(self):
        with_wrap = False
        if self.can_wrap:
            real_xVel=self.xVel
            if self.x+self.xVel<self.level.x:
                perc_xvel = max(0, self.level.xVel)
                self.x+=perc_xvel
                self.xVel-=perc_xvel

                with_wrap=True
                self.move([
                    (self.level.x, self.level.x+self.w, self.level.x),
                    (self.x+self.level.screenSize.x+self.xVel,
                        self.level.x+self.level.screenSize.x, self.x+self.xVel)])
            elif self.x+self.w+self.xVel>self.level.x+self.level.screenSize.x:
                perc_xvel = min(0, self.level.xVel)
                self.x+=perc_xvel
                self.xVel-=perc_xvel

                with_wrap=True
                self.move([
                    (self.x, self.level.x+self.level.screenSize.x, self.x),
                    (self.level.x, self.level.x*2-self.level.screenSize.x+self.x+self.w+self.xVel,
                        self.level.x+self.level.screenSize.x)])
            if self.xVel != 0 and with_wrap: self.xVel = real_xVel
        if not with_wrap:
            self.move([(self.x+min(0, self.xVel), self.x+self.w+max(0,self.xVel), self.x+min(0, self.xVel))])

        self.xVel *= 0.95
        self.yVel *= 0.98

        if abs(self.xVel) <= 0.002: self.xVel = 0
        if abs(self.yVel) <= 0.002: self.yVel = 0

    def move(self, slices):
        # slices:[
        #     (x1,x2,pos)
        # ]
        collidables = []
        for slice in slices:
            for entity in self.level.entities:
                if entity is self or not entity.solid: continue
                if slice[0]-entity.w <= entity.x <= slice[1]:
                    x=max(entity.x,slice[0])
                    x2=min(entity.x+entity.w,slice[1])
                    collidables.append(Rect(x+(slice[2]-slice[0]),entity.y,x2-x,entity.h))

        self.normal = Vector(0, 0)
        remainingXVel = self.xVel
        remainingYVel = self.yVel

        maxCount = 2
        while (remainingXVel != 0 or remainingYVel != 0) and maxCount > 0:
            closestPoint = {
                "point": Vector(
                    self.x + remainingXVel,
                    self.y + remainingYVel
                ),
                "normal": Vector(0, 0),
                "distance": 1
            }

            for other in collidables:
                contact = False
                if remainingYVel == 0 or remainingXVel == 0:
                    if (other.x - self.w - abs(remainingXVel) <=
                            min(self.x, self.x + remainingXVel) <= other.x + other.w and
                            other.y - self.h - abs(remainingYVel) <=
                            min(self.y, self.y + remainingYVel) <= other.y + other.h):
                        point = Vector(self.x, self.y)
                        normal = Vector(0, 0)
                        if remainingYVel != 0:
                            point.y = other.y + (-self.h if remainingYVel > 0 else other.h)
                            normal.y = -1 if remainingYVel > 0 else 1
                        if remainingXVel != 0:
                            point.x = other.x + (-self.w if remainingXVel > 0 else other.w)
                            normal.x = -1 if remainingXVel > 0 else 1

                        contact = {
                            'point': point,
                            'normal': normal,
                            'distance': -(point.x - self.x + point.y - self.y) / abs(remainingXVel + remainingYVel)
                        }
                else:
                    contact = isRayInRect(Vector(self.x, self.y), Vector(remainingXVel, remainingYVel),
                                          Rect(other.x - self.w, other.y - self.h, other.w + self.w, other.h + self.h))

                if contact is not False and contact['distance'] < closestPoint['distance']:
                    closestPoint = contact

            remainingXVel -= round((closestPoint['point'].x - self.x) / epsilon) * epsilon
            remainingYVel -= round((closestPoint['point'].y - self.y) / epsilon) * epsilon

            self.x = round((closestPoint['point'].x + closestPoint['normal'].x * epsilon) / epsilon) * epsilon
            self.y = round((closestPoint['point'].y + closestPoint['normal'].y * epsilon) / epsilon) * epsilon

            remainingXVel *= -abs(closestPoint['normal'].x) + 1
            remainingYVel *= -abs(closestPoint['normal'].y) + 1

            maxCount -= 1

            self.normal.x = self.normal.x if self.normal.x != 0 else closestPoint['normal'].x
            self.normal.y = self.normal.y if self.normal.y != 0 else closestPoint['normal'].y
            if closestPoint['normal'].x != 0:
                self.xVel = 0
            if closestPoint['normal'].y != 0:
                self.yVel = 0

    # def render(self):
    #     pygame.draw.rect(self.level.surface, (255,0,0), (self.x,self.y,self.w,self.h))


def init():
    def loader(strings):
        return SolidEntity(int(strings[0]), int(strings[1]), int(strings[2]), int(strings[3]))
    level_loader.ENTITY_LOADERS['solid'] = loader
