#!/usr/bin/env python
"""Functions and classes used for the game's color choice menu. This file can also be run on it's
own to start the game from here."""
import button
import game
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    Rect,
    QUIT, MOUSEBUTTONDOWN, KEYDOWN,
    K_m)

class ColorChoice(game.GameState):
    """The class for the color choice of the game."""
    caption = "OmniTank Color Choice"
    img_assets = {
        "icon": "icon.png",
        "background": "tank_color.png",
        "outline": "selection_outline.png",
        "tank_outline": "tank_outline.png",
    }
    snd_assets = {
        "rollover": "menu_rollover.wav",
        "click": "menu_click.wav",
    }

    def __init__(self, display, clock):
        super().__init__(display, clock)
        self.music_paused = False

    def setup(self):
        super().setup()
        pygame.mouse.set_visible(True)

        btn_size = (290, 40)
        btn_size2 = (120, 150)
        y_value = 310
        outline = self.img("outline")
        outline2 = self.img("tank_outline")
        self.btn_group.add(button.Outline("return", Rect((634, 526), btn_size), outline))
        self.btn_group.add(button.Outline("blue", Rect((152, y_value), btn_size2), outline2))
        self.btn_group.add(button.Outline("red", Rect((302, y_value), btn_size2), outline2))
        self.btn_group.add(button.Outline("green", Rect((452, y_value), btn_size2), outline2))
        self.btn_group.add(button.Outline("dark", Rect((602, y_value), btn_size2), outline2))
        self.btn_group.add(button.Outline("light", Rect((752, y_value), btn_size2), outline2))

        self.snd("rollover").set_volume(0.5)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN and self.hovered_btns:
                self.snd("click").play()
                clicked = self.hovered_btns[0]
                if clicked.name == "return":
                    self.running = False
                # else:
                #     game(clicked.name)
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.music_paused = not self.music_paused
                    if self.music_paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

def main():
    """Sets up pygame and runs the color choice menu."""
    display, clock = game.init_pygame()
    color_choice = ColorChoice(display, clock)
    color_choice.run()

if __name__ == "__main__":
    main()
