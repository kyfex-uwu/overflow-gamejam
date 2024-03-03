import level_loader
from entity.entity import Entity


class SpawnPointEntity(Entity):
    def __init__(self, x, y, w, h, spawnpoint):
        super().__init__(x, y, w, h)
        self.spawnpoint = spawnpoint

    def init(self, level):
        super().init(level)
        if level.default_spawn is None:
            level.default_spawn = self.spawnpoint
            if level.player_entity is not None:
                level.player_entity.spawnpoint = self.spawnpoint
                level.player_entity.x=level.player_entity.spawnpoint[0]
                level.player_entity.y=level.player_entity.spawnpoint[1]

    def tick(self):
        if self.level.player_entity is not None and self.colliding(self.level.player_entity):
            self.level.player_entity.spawnpoint = self.spawnpoint

    def render(self):
        pass

def init():
    def loader(strings):
        return SpawnPointEntity(int(strings[0]), int(strings[1]), int(strings[2]), int(strings[3]),
                                (int(strings[4]), int(strings[5])))
    level_loader.ENTITY_LOADERS['spawn'] = loader
