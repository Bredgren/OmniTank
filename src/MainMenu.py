#!/usr/bin/env python
"""Functions and classes used for the game's main menu. This file can also be run on it's
own to start the game from the main menu."""
import time
import button
import data
import game
from ColorChoice import ColorChoice
from Instructions import Instructions
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    Rect,
    QUIT, MOUSEBUTTONDOWN, KEYDOWN,
    K_m)

class MainMenu(game.GameState):
    """The class for the main menu of the game."""
    caption = "OmniTank Menu"
    img_assets = {
        "icon": "icon.png",
        "background": "main_menu.png",
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
        data.load_music("Mechanolith.mp3")
        pygame.mixer.music.play(-1)

        btn_size = (290, 40)
        outline = self.img("outline")
        self.btn_group.add(button.Outline("start", Rect((367, 311), btn_size), outline))
        self.btn_group.add(button.Outline("instructions", Rect((367, 363), btn_size), outline))
        self.btn_group.add(button.Outline("highscores", Rect((367, 413), btn_size), outline))
        self.btn_group.add(button.Outline("quit", Rect((367, 465), btn_size), outline))

        self.snd("rollover").set_volume(0.5)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN and self.hovered_btns:
                self.snd("click").play()
                clicked = self.hovered_btns[0]
                if clicked.name == "start":
                    color_choice = ColorChoice(self.display, self.clock)
                    color_choice.run()
                elif clicked.name == "instructions":
                    i = Instructions(self.display, self.clock)
                    i.run()
                elif clicked.name == "highscores":
                    pass
                elif clicked.name == "quit":
                    self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.music_paused = not self.music_paused
                    if self.music_paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

    def on_exit(self):
        time.sleep(0.5)
        print("Bye")

def main():
    """Sets up pygame and runs the main menu."""
    display, clock = game.init_pygame()
    main_menu = MainMenu(display, clock)
    main_menu.run()

if __name__ == "__main__":
    main()
