import pygame

CURR_SCREEN = None
SCREEN = None

def set_size(size):
    global PIXEL_WIDTH
    global SCREEN
    PIXEL_WIDTH = size
    SCREEN = pygame.display.set_mode((PIXEL_WIDTH * 11 * 16, PIXEL_WIDTH * 11 * 9))

LEVELS_UNLOCKED = 1
CURR_LEVEL = -1
FINISHED=False
def finish_level():
    global LEVELS_UNLOCKED
    LEVELS_UNLOCKED = max(LEVELS_UNLOCKED, CURR_LEVEL+1)

PIXEL_WIDTH=8

MOUSE = {
    "left": False,
    "right": False,
    "p_left": False,
    "p_right": False
}

TIMER = 0

IMAGES = {}
SCREEN_CONSTRS={}
