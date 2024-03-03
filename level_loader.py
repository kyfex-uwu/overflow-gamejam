import os.path

from level import Level

ENTITY_LOADERS = {}

def load_level(level_name):
    with open(os.path.join("resources", "levels", level_name + ".txt"), encoding="utf-8") as levelfile:
        leveldata = [line.split(";") for line in levelfile.read().split("\n")]
        # metadata
        to_return = Level(int(leveldata[0][0]), int(leveldata[0][1]))

        # tile palette
        palette = {".": None}
        images = set()
        for img_group in leveldata[2]:
            data = img_group.split(":", 1)
            images.add(data[0])
            these_tiles = [data[1][i:i + 3] for i in range(0, len(data[1]), 3)]
            for tile in these_tiles:
                palette[tile[0]] = (int(tile[1]), int(tile[2]), data[0])

        # tiles
        width = sorted([len(line) for line in leveldata[3]], key=lambda e: e, reverse=True)[0]
        for i in range(len(leveldata[3])):
            leveldata[3][i] = leveldata[3][i] + ("." * (width - len(leveldata[3][i])))
        ENTITY_LOADERS['tiles'](([[palette[char] for char in line] for line in leveldata[3]], images)
                                ).init(to_return)

        # entities
        entities = []
        for entity_str in leveldata[1]:
            data = entity_str.split(":", 1)
            entities.append(ENTITY_LOADERS[data[0]](data[1].split(",")))
        for entity in entities:
            entity.init(to_return)
        ENTITY_LOADERS['player'](()).init(to_return)

        return to_return
