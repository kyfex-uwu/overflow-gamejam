from screen.screen import Screen
import audio

class TitleScreen(Screen):
    def __init__(self, args):
        super().__init__(args)
        audio.title()
    def render(self, screen):
        pass