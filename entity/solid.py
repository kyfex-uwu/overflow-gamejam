from entity.entity import Entity, Point, Rect


def isRayInRect(rayOrigin:Point, rayDir:Point, rect:Rect):
    if rayDir.x == 0: rayDir.x = 0.00001
    if rayDir.y == 0: rayDir.y = 0.00001

    tNear = Point(
        (rect.x - rayOrigin.x) / rayDir.x,
        (rect.y - rayOrigin.y) / rayDir.y
    )
    tFar = Point(
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

    contactPoint = Point(
        rayOrigin.x + tHitNear * rayDir.x,
        rayOrigin.y + tHitNear * rayDir.y
    )
    contactNormal = Point(0,0)
    if tNear.x > tNear.y:
        if rayDir.x < 0:
            contactNormal = Point(1,0)
        else:
            contactNormal = Point(-1,0)
    elif tNear.x < tNear.y:
        if rayDir.y < 0:
            contactNormal = Point(0,1)
        else:
            contactNormal = Point(0,-1)
    return {
        'point': contactPoint,
        'normal': contactNormal,
        'distance': tHitNear
    }

class SolidEntity(Entity):
    def __init__(self, x, y, w, h, weight):
        super().__init__(x, y, w, h)
        self.weight=weight

    def tick(self):
        self.move()
        self.xVel*=0.9
        self.yVel*=0.95

    def move(self):

        remainingXVel = self.xVel
        remainingYVel = self.yVel

        maxCount = 2
        while (remainingXVel != 0 or remainingYVel != 0) and maxCount > 0:
            closestPoint={
                "point":Point(
                    self.x + remainingXVel,
                    self.y + remainingYVel
                ),
                "normal": Point(0,0),
                "distance": 1
            }

            for other in self.level.entities:
                if other is self: continue

                contact = isRayInRect(Point(self.x,self.y), Point(remainingXVel,remainingYVel),
                                      Rect(other.x - self.w, other.y - self.h, other.w + self.w, other.h + self.h))
                if contact is not False and contact['distance'] < closestPoint['distance']:
                    closestPoint=contact

            remainingXVel -= round((closestPoint['point'].x-self.x) * 1000) / 1000
            remainingYVel -= round((closestPoint['point'].y-self.y) * 1000) / 1000

            self.x=round((closestPoint['point'].x+closestPoint['normal'].x * 0.001) * 1000) / 1000
            self.y=round((closestPoint['point'].y+closestPoint['normal'].y * 0.001) * 1000) / 1000

            remainingXVel *= -abs(closestPoint['normal'].x)+1
            remainingYVel *= -abs(closestPoint['normal'].y)+1

            maxCount-=1

        self.xVel = round(self.xVel * 0.8 * 1000) / 1000
        self.yVel = round(self.yVel * 0.8 * 1000) / 1000

        if abs(self.xVel) <= 0.002: self.xVel=0
        if abs(self.yVel) <= 0.002: self.yVel=0
