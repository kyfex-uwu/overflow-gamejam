from pygame import Surface

import audio
import font
import globalvars
from screen.component.button import Button
from screen.component.wrap_img import WrapImage
from screen.level import drawTimer
from screen.screen import Screen
import webbrowser
import requests
import asyncio
import json

outdated=False
this_version="0.9.0"
async def main():
    response = requests.get("https://itch.io/api/1/x/wharf/latest?target=kyfex-uwu/wraparound&channel_name="
                            "windows"
                            )
    try:
        if json.loads(response.text)["latest"] != this_version:
            global outdated
            outdated=True
    except:
        pass
asyncio.run(main())

class TitleScreen(Screen):
    def __init__(self, args: tuple):
        super().__init__(args)
        self.wrap_amt = 0
        audio.title()

        self.components.append(WrapImage("title",2))

        def on_click():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["select"](
                (globalvars.LEVELS_UNLOCKED-1,globalvars.LEVELS_UNLOCKED-1))
        self.components.append(Button(75,50,27,27, on_click))

        def on_click2():
            globalvars.CURR_SCREEN = globalvars.SCREEN_CONSTRS["settings"](())
        self.components.append(Button(25,50,27,27, on_click2))

        def on_click3():
            if not outdated: return
            webbrowser.open('https://kyfex-uwu.itch.io/wraparound')
        self.components.append(Button(176-15*6-2,80, 176,19, on_click3))


    def render(self, screen: Surface):
        self.screen = screen
        screen.fill((30,30,60))
        super().render(screen)

        self.screen.blit(globalvars.IMAGES["buttons"], (75,50), (27,81, 27, 27))
        self.screen.blit(globalvars.IMAGES["buttons"], (25,50), (54,81, 27, 27))

        if globalvars.FINISHED is not False:
            drawTimer(round(globalvars.FINISHED * 1000), self.screen, (0, 200, 0))

        if outdated:
            font.write(self.screen, "new version!\nClick to update", 176,80,centered=2)
        else:
            font.write(self.screen, "v"+this_version, 176, 90, centered=2)

        # if keys.DEV_UNLOCK.pressed:
        #     globalvars.LEVELS_UNLOCKED = 16
        #     globalvars.TIMER = 999999
        if keys.LEVEL_EDITOR.pressed:
            pass
