from entity.entity import Entity, Vector, Rect

epsilon=0.00001
inv_epsilon = 1/epsilon
def isRayInRect(rayOrigin:Vector, rayDir:Vector, rect:Rect):
    if rayDir.x == 0: rayDir.x = epsilon
    if rayDir.y == 0: rayDir.y = epsilon

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
        self.grounded=False

    def tick(self):
        self.move()

        self.xVel *= 0.95
        self.yVel *= 0.98

        if abs(self.xVel) <= 0.002: self.xVel=0
        if abs(self.yVel) <= 0.002: self.yVel=0

    def move(self):
        self.grounded=False
        remainingXVel = self.xVel
        remainingYVel = self.yVel

        maxCount = 2
        while (remainingXVel != 0 or remainingYVel != 0) and maxCount > 0:
            closestPoint={
                "point":Vector(
                    self.x + remainingXVel,
                    self.y + remainingYVel
                ),
                "normal": Vector(0, 0),
                "distance": 1
            }

            for other in self.level.entities:
                if other is self: continue

                contact = isRayInRect(Vector(self.x, self.y), Vector(remainingXVel, remainingYVel),
                                      Rect(other.x - self.w, other.y - self.h, other.w + self.w, other.h + self.h))
                if contact is not False and contact['distance'] < closestPoint['distance']:
                    closestPoint=contact

            remainingXVel -= round((closestPoint['point'].x-self.x) / epsilon) * epsilon
            remainingYVel -= round((closestPoint['point'].y-self.y) / epsilon) * epsilon

            self.x=round((closestPoint['point'].x+closestPoint['normal'].x * epsilon) / epsilon) * epsilon
            self.y=round((closestPoint['point'].y+closestPoint['normal'].y * epsilon) / epsilon) * epsilon

            remainingXVel *= -abs(closestPoint['normal'].x)+1
            remainingYVel *= -abs(closestPoint['normal'].y)+1

            maxCount-=1

            self.grounded = self.grounded or closestPoint['normal'].y==-1
            if closestPoint['normal'].x != 0:
                self.xVel=0
            if closestPoint['normal'].y != 0:
                self.yVel=0
