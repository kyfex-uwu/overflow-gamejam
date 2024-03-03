from screen.screen import Screen


class LevelScreen(Screen):
    def __init__(self, args):
        super().__init__(args)
        self.level = args[0]
    def render(self, screen):
        self.level.tick()
        self.level.render(screen)