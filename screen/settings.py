from screen.component.wrap_img import WrapImage
from screen.screen import Screen


class SettingsScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)

        self.components.append(WrapImage("settings",3))

    def render(self, screen):
        screen.fill((30,30,60))
        
        super().render(screen)