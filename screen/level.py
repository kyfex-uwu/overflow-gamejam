from screen.screen import Screen
import audio


class LevelScreen(Screen):
    def __init__(self, args):
        super().__init__(args)
        self.level = args[0]
        audio.playLevel()
    def render(self, screen):
        self.level.tick()
        self.level.render(screen)