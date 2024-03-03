

class Screen:
    def __init__(self, args:tuple):
        self.components = []
    def render(self, screen):
        for component in self.components:
            component.render(screen)
