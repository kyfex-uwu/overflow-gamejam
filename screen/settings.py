import globalvars
from screen.component.button import Button
from screen.component.wrap_img import WrapImage
from screen.screen import Screen


class SettingsScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)

        self.components.append(WrapImage("settings",3))
        def back():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["title"](())
        self.components.append(Button(5, 79,19,15, back))

    def render(self, screen):
        screen.fill((30,30,60))
        
        super().render(screen)
        screen.blit(globalvars.IMAGES["buttons"], (5, 79), (29,110, 19,15))