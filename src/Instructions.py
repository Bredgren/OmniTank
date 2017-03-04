#!/usr/bin/env python
"""Functions and classes used for showing the game's instructions. This file can also
be run on it's own to start the game from the instructions windowws."""
import button
import game
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    Rect,
    MOUSEBUTTONDOWN, KEYDOWN,
    K_m)

class Instructions(game.GameState):
    """The class for the instructions of the game."""
    caption = "OmniTank Instructions"
    img_assets = {
        "icon": "icon.png",
        "background": "instructions.png",
        "outline": "selection_outline.png",
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
        outline = self.img("outline")
        self.btn_group.add(button.Outline("return", Rect((676, 39), btn_size), outline))

        self.snd("rollover").set_volume(0.5)

    def update(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and self.hovered_btns:
                self.snd("click").play()
                clicked = self.hovered_btns[0]
                if clicked.name == "return":
                    self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.music_paused = not self.music_paused
                    if self.music_paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

def main():
    """Sets up pygame and runs the instructions."""
    display, clock = game.init_pygame()
    i = Instructions(display, clock)
    i.run()

if __name__ == "__main__":
    main()
