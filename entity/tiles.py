from entity.solid import SolidEntity


class Tiles(SolidEntity):
    def __init__(self, palette, tileStr:str):
        super().__init__(0, 0, 0, 0)
        self.palette = palette

        rows = tileStr.split("\n")
        self.tiles = [[None]*len(rows[0]) for _ in rows]

    def render(self):
        pass