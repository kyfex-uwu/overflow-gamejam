CURR_SCREEN = None

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
