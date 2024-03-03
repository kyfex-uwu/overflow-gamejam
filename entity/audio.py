import os
from pygame import mixer


mixer.init()
class audioRunner:
    def __init__(self):
        #channel 1 is for main music
        #channel 2 is for sound effects
        mixer.Channel(1)
        mixer.Channel(2)
        self.mainTheme = mixer.Sound(os.path.join("resources", "audio", "Platforms-in-the-Sky.ogg"))
        self.levelComplete = mixer.Sound(os.path.join("resources", "audio", "Level-Complete.ogg"))
    
    def mainTheme(self):
        mixer.Channel(1).play(self.mainTheme, loops= -1)

    def collect(self):
        mixer.Channel(2).play(self.levelComplete)