import pygame


_all_keys = []
class KeyData:
    def __init__(self, key):
        self.key=key
        self.down=False
        self.pressed=False
        self.released=False
        _all_keys.append(self)

LEFT = KeyData(pygame.K_a)
RIGHT = KeyData(pygame.K_d)
JUMP = KeyData(pygame.K_w)
SCR_LEFT = KeyData(pygame.K_LEFT)
SCR_RIGHT = KeyData(pygame.K_RIGHT)
PAUSE = KeyData(pygame.K_ESCAPE)

DEV_UNLOCK = KeyData(pygame.K_o)

def poll():
    keys = pygame.key.get_pressed()
    for key in _all_keys:
        key.pressed=False
        key.released=False
        if keys[key.key]:
            if not key.down: key.pressed = True
            key.down=True
        else:
            if key.down: key.released = True
            key.down=False
