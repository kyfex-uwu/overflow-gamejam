import os
from pygame import mixer


mixer.init()


#channel 1 is for main music
#channel 2 is for sound effects
mixer.Channel(1)
mixer.Channel(2)

#music
mainTheme = mixer.Sound(os.path.join("resources", "audio", "Platforms-in-the-Sky.ogg"))
levelComplete = mixer.Sound(os.path.join("resources", "audio", "Level-Complete.ogg"))

def playLevel():
    mixer.Channel(1).play(mainTheme, loops= -1)

def collect():
    mixer.Channel(1).stop()
    mixer.Channel(2).set_volume(1)
    mixer.Channel(2).play(levelComplete)