import pygame


all_keys = []
class KeyData:
    def __init__(self, key, name):
        self.key=key
        self.name=name
        self.down=False
        self.pressed=False
        self.released=False
        all_keys.append(self)

LEFT = KeyData(pygame.K_a, "Left")
RIGHT = KeyData(pygame.K_d, "Right")
JUMP = KeyData(pygame.K_w, "Jump")
SCR_LEFT = KeyData(pygame.K_LEFT, "S Left")
SCR_RIGHT = KeyData(pygame.K_RIGHT, "S Right")
PAUSE = KeyData(pygame.K_ESCAPE, "Pause")
# make sure to give the key a name! the first key without a name signifies dev keys
DEV_UNLOCK = KeyData(pygame.K_o, "")
LEVEL_EDITOR = KeyData(pygame.K_l, "")

def poll():
    keys = pygame.key.get_pressed()
    for key in all_keys:
        key.pressed=False
        key.released=False
        if keys[key.key]:
            if not key.down: key.pressed = True
            key.down=True
        else:
            if key.down: key.released = True
            key.down=False
