import os

import pygame
from pygame import Surface

import audio
import globalvars
import level_loader
from screen.level import LevelScreen
from screen.title import TitleScreen

# pygame setup
pygame.init()
pygame.display.set_caption('wraparound')
SMALL_SCREEN = Surface((11 * 16, 11 * 9))
LEVELS_UNLOCKED = 1
clock = pygame.time.Clock()
running = True
dt = 0

# config init
def set_vol(args):
    globalvars.CONFIG["volume"] = min(1,max(0,float(args[0])))
def set_size(args):
    globalvars.CONFIG["size"] = max(0,min(8,int(args[0])))+1
with open("conf.txt", "r+") as config:
    for prop in config.readlines():
        try:
            data = prop.split(": ",1)
            ({
                "volume": set_vol,
                "size": set_size
            })[data[0]](data[1:])
        except Exception:
            pass
globalvars.set_size(globalvars.CONFIG["size"])
audio.music_vol(globalvars.CONFIG["volume"])

from entity import disk, player, solid, spawn, tiles, spikes, display

for entity in {disk, player, solid, spawn, tiles, spikes, display}:
    entity.init()

from screen import level, select, settings, title, credits

globalvars.SCREEN_CONSTRS["level"] = level.LevelScreen
globalvars.SCREEN_CONSTRS["select"] = select.SelectScreen
globalvars.SCREEN_CONSTRS["settings"] = settings.SettingsScreen
globalvars.SCREEN_CONSTRS["title"] = title.TitleScreen
globalvars.SCREEN_CONSTRS["credits"] = credits.CreditsScreen

#globalvars.CURR_SCREEN = TitleScreen(())
globalvars.CURR_SCREEN = LevelScreen((level_loader.load_level("test4"),))
globalvars.IMAGES = {
    "buttons": pygame.image.load(os.path.join('resources', 'buttons.png')).convert_alpha(),
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    globalvars.MOUSE["p_left"] = globalvars.MOUSE["left"]
    globalvars.MOUSE["p_right"] = globalvars.MOUSE["right"]
    state = pygame.mouse.get_pressed(3)
    globalvars.MOUSE["left"] = state[0]
    globalvars.MOUSE["right"] = state[2]

    if isinstance(globalvars.CURR_SCREEN, LevelScreen) and not globalvars.CURR_SCREEN.level.finished:
        globalvars.TIMER += dt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_o]:
        globalvars.LEVELS_UNLOCKED = 16
        globalvars.TIMER = 999999

    globalvars.CURR_SCREEN.render(SMALL_SCREEN)
    pygame.transform.scale(SMALL_SCREEN, globalvars.SCREEN.get_size(), globalvars.SCREEN)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()

with open("conf.txt", "w") as config:
    config.write("\nvolume: "+str(globalvars.CONFIG["volume"]))
    config.write("\nsize: "+str(globalvars.CONFIG["size"]))
