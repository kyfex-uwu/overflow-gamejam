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
titleTheme = mixer.Sound(os.path.join("resources", "audio", "Title.ogg"))
hit = mixer.Sound(os.path.join("resources", "audio", "Hit.ogg"))
glitch = mixer.Sound(os.path.join("resources", "audio", "ERROR-OVERFLOW.ogg"))
collect2 = mixer.Sound(os.path.join("resources", "audio", "1-Complete.ogg"))

#variables
check1 = False

def playLevel():
    global check1
    if check1:
        check1 = False
    mixer.Channel(1).stop()
    mixer.Channel(1).play(mainTheme, loops= -1)

def collect():
    mixer.Channel(1).stop()
    mixer.Channel(2).set_volume(1)
    mixer.Channel(2).play(levelComplete)

def title():
    global check1
    if not check1:
        check1 = True
        mixer.Channel(1).stop()
        mixer.Channel(1).play(titleTheme, loops= -1)

def hurt():
    mixer.Channel(2).play(hit)

def glitched():
    global check1
    if check1:
        check1 = False
    mixer.Channel(1).stop()
    mixer.Channel(1).play(glitch, loops= -1)

def win():
    mixer.Channel(1).stop()
    mixer.Channel(2).set_volume(1)
    mixer.Channel(2).play(collect2)

def music_vol(vol):
    if vol is not None:
        mixer.Channel(1).set_volume(vol)
    return mixer.Channel(1).get_volume()
def sfx_vol(vol):
    if vol is not None:
        mixer.Channel(2).set_volume(vol)
    return mixer.Channel(2).get_volume()
