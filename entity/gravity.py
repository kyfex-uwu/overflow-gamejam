from entity.solid import SolidEntity


class GravityEntity(SolidEntity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def tick(self):
        self.xVel = (1 if self.xVel>=0 else -1) * min(abs(self.xVel), 3)
        self.yVel = (1 if self.yVel+0.23>=0 else -1) * min(abs(self.yVel+0.23), 5)
        super().tick()
